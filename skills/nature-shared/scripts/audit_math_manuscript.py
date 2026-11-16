#!/usr/bin/env python3
"""Conservative structural audit of a mathematics (theory/proof) LaTeX manuscript.

The audit locates things a mathematics referee must check. It does not decide whether a
proof is correct.

- theorem-like statements, their labels and the proof that follows each;
- references and citations that do not resolve, and duplicate labels;
- the proof-dependency graph (statement -> results cited inside its proof), its cycles and
  forward references;
- silent conditions: a statement whose dependency closure contains an unproved node
  (conjecture/hypothesis environment) but which names no condition;
- hand-waving markers ("clearly", "it is easy to see", ...) and TODO markers;
- whether the abstract mentions conditions when some statement is conditional.

Exit status: 0 no errors, 1 errors found, 2 cannot audit.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

PROOF_KINDS = {"theorem", "proposition", "lemma", "corollary", "claim"}
UNPROVED_KINDS = {"conjecture", "hypothesis", "assumption", "question", "problem"}
DEFAULT_ENVS = {
    "theorem": "theorem", "thm": "theorem", "proposition": "proposition", "prop": "proposition",
    "lemma": "lemma", "lem": "lemma", "corollary": "corollary", "cor": "corollary",
    "claim": "claim", "conjecture": "conjecture", "conj": "conjecture",
    "hypothesis": "hypothesis", "definition": "definition", "defn": "definition",
    "remark": "remark", "rem": "remark", "example": "example", "question": "question",
    "problem": "problem", "assumption": "assumption",
}
HANDWAVE = (
    "clearly", "obviously", "it is easy to see", "it is easy to check", "trivially",
    "it is straightforward", "straightforward to verify", "the same argument shows",
    "similarly one shows", "routine", "left to the reader", "one easily checks",
)
CONDITION_WORDS = ("assum", "condition", "hypothes", "provided", "conjectur", "if (", "under (")
TODO_RE = re.compile(r"\\todo\b|\bTODO\b|\bFIXME\b|\bXXX\b|\?\?")
INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")
NEWTHEOREM_RE = re.compile(r"\\newtheorem\*?\s*\{([^}]+)\}(?:\s*\[[^\]]*\])?\s*\{([^}]+)\}")
BEGIN_END_RE = re.compile(r"\\(begin|end)\s*\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\s*\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|cref|Cref|autoref|pageref|nameref)\s*\{([^}]+)\}")
CITE_RE = re.compile(r"\\(?:cite|citet|citep|citealp|nocite|parencite|textcite)\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}")
BIBITEM_RE = re.compile(r"\\bibitem\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}")
BIBLIOGRAPHY_RE = re.compile(r"\\(?:bibliography|addbibresource)\s*\{([^}]+)\}")
PROOF_OF_RE = re.compile(r"\s*\[((?:[^\[\]]|\[[^\]]*\])*)\]")
PARAGRAPH_PROOF_RE = re.compile(
    r"\\(?:emph|textit|textbf|paragraph|section|subsection|subsubsection)\*?\s*\{\s*Proofs? of (?:the )?(?:Theorem|Proposition|Lemma|Corollary|Claim)s?"
    r"[~\s]*\\(?:ref|cref|Cref)\s*\{([^}]+)\}", re.IGNORECASE)
RESTATEMENT_RE = re.compile(
    r"\\end\s*\{[^}]+\}\s*(?:This|It) is (?:a special case of |part of )?(?:Theorem|Proposition|Corollary|Lemma)"
    r"[~\s]*\\(?:ref|cref|Cref)\s*\{([^}]+)\}")
BIBENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")


@dataclass
class Statement:
    sid: int
    env: str
    kind: str
    file: str
    line: int
    labels: list[str] = field(default_factory=list)
    text: str = ""
    proof_refs: list[str] = field(default_factory=list)
    restates: list[str] = field(default_factory=list)
    has_proof: bool = False
    cites_in_statement: bool = False


def strip_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in text.split("\n"))


def load(path: Path, seen: set[Path], chunks: list[tuple[str, int, str]]) -> None:
    """Expand \\input/\\include into (file, first_line, text) chunks in document order."""
    path = path.resolve()
    if path in seen:
        return
    seen.add(path)
    text = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
    pos, line = 0, 1
    for match in INPUT_RE.finditer(text):
        before = text[pos:match.start()]
        chunks.append((str(path), line, before))
        line += before.count("\n")
        name = match.group(1).strip()
        target = (path.parent / name)
        if target.suffix != ".tex":
            target = target.with_suffix(".tex") if not target.exists() else target
        if target.exists():
            load(target, seen, chunks)
        else:
            chunks.append((str(path), line, f"\\MISSINGINPUT{{{name}}}"))
        line += match.group(0).count("\n")
        pos = match.end()
    chunks.append((str(path), line, text[pos:]))


def audit(main: Path) -> dict[str, Any]:
    chunks: list[tuple[str, int, str]] = []
    load(main, set(), chunks)
    findings: list[dict[str, Any]] = []

    def find(code: str, severity: str, message: str, file: str, line: int, token: str | None = None) -> None:
        findings.append({"code": code, "severity": severity, "file": Path(file).name, "line": line,
                         "token": token, "message": message})

    envs = dict(DEFAULT_ENVS)
    for file, start, text in chunks:
        for m in NEWTHEOREM_RE.finditer(text):
            name, title = m.group(1).strip(), m.group(2).strip().lower()
            kind = next((k for k in (*PROOF_KINDS, *UNPROVED_KINDS, "definition", "remark", "example")
                         if k in title), "other")
            envs[name] = kind
    statements: list[Statement] = []
    labels: dict[str, tuple[str, int, int | None]] = {}   # label -> (file, line, statement id)
    refs: list[tuple[str, str, int, int | None, bool]] = []  # (label, file, line, owner sid, in proof)
    cites: list[tuple[str, str, int]] = []
    bib_keys: set[str] = set()
    bib_sources = False
    abstract_text = ""
    stack: list[tuple[str, Statement | None]] = []
    last_statement: Statement | None = None
    order: dict[str, int] = {}   # label -> document position
    position = 0
    deferred: list[Statement] = []   # proofs naming a statement that appears later

    for file, start, text in chunks:
        if "\\MISSINGINPUT" in text:
            for m in re.finditer(r"\\MISSINGINPUT\{([^}]*)\}", text):
                find("missing_input", "error", "an \\input file could not be found", file, start, m.group(1))
        for m in BIBITEM_RE.finditer(text):
            bib_keys.add(m.group(1).strip()); bib_sources = True
        for m in BIBLIOGRAPHY_RE.finditer(text):
            for name in m.group(1).split(","):
                bib = (Path(file).parent / name.strip())
                bib = bib if bib.suffix == ".bib" else bib.with_suffix(".bib")
                if bib.exists():
                    bib_sources = True
                    bib_keys |= {k.strip() for k in BIBENTRY_RE.findall(bib.read_text(encoding="utf-8", errors="replace"))}
        tokens = sorted(
            [(m.start(), "env", m) for m in BEGIN_END_RE.finditer(text)]
            + [(m.start(), "label", m) for m in LABEL_RE.finditer(text)]
            + [(m.start(), "ref", m) for m in REF_RE.finditer(text)]
            + [(m.start(), "cite", m) for m in CITE_RE.finditer(text)],
            key=lambda item: item[0])
        segment_start = 0
        for offset, kind, m in tokens:
            line = start + text.count("\n", 0, offset)
            position += 1
            current = next((s for _, s in reversed(stack) if s is not None), None)
            in_proof = any(name == "proof" for name, _ in stack)
            if current is not None and not in_proof:
                current.text += text[segment_start:offset]
            if any(name == "abstract" for name, _ in stack):
                abstract_text += text[segment_start:offset]
            segment_start = offset
            if kind == "env":
                action, name = m.group(1), m.group(2).strip()
                if action == "begin":
                    if name in envs or name.rstrip("*") in envs:
                        env = name.rstrip("*")
                        st = Statement(len(statements), env, envs[env], file, line)
                        statements.append(st)
                        stack.append((name, st))
                        last_statement = st
                    elif name == "proof":
                        # "\begin{proof}[Proof of Theorem~\ref{x}]" proves x, wherever x was stated
                        named = PROOF_OF_RE.match(text, m.end())
                        target_label = None
                        if named:
                            inner = REF_RE.search(named.group(1))
                            target_label = inner.group(1).split(",")[0].strip() if inner else None
                        target = None
                        if target_label is not None:
                            info = labels.get(target_label)
                            target = statements[info[2]] if info and info[2] is not None else None
                            if target is None:
                                target = Statement(-1, "deferred", "deferred", file, line, [target_label])
                                deferred.append(target)
                        if target is not None:
                            target.has_proof = True
                            stack.append(("proof", target))
                        elif last_statement is not None and not last_statement.has_proof:
                            last_statement.has_proof = True
                            stack.append(("proof", last_statement))
                        else:
                            stack.append(("proof", None))
                            find("orphan_proof", "warning", "proof environment not attached to a preceding statement",
                                 file, line)
                    else:
                        stack.append((name, None))
                else:
                    for i in range(len(stack) - 1, -1, -1):
                        if stack[i][0] == name:
                            del stack[i:]
                            break
            elif kind == "label":
                label = m.group(1).strip()
                owner = next((s for n, s in reversed(stack) if s is not None and n != "proof"), None)
                if label in labels:
                    find("duplicate_label", "error", "label defined more than once", file, line, label)
                labels[label] = (file, line, owner.sid if owner else None)
                order.setdefault(label, position)
                if owner is not None:
                    owner.labels.append(label)
            elif kind == "ref":
                owner = next((s for n, s in reversed(stack) if s is not None), None)
                for label in m.group(1).split(","):
                    label = label.strip()
                    refs.append((label, file, line, owner.sid if owner else None, in_proof))
                    if in_proof and owner is not None:
                        owner.proof_refs.append(label)
            elif kind == "cite":
                for key in m.group(1).split(","):
                    cites.append((key.strip(), file, line))
                owner = next((s for n, s in reversed(stack) if s is not None and n != "proof"), None)
                if owner is not None and not in_proof:
                    owner.cites_in_statement = True
        if stack and stack[-1][1] is not None:
            stack[-1][1].text += text[segment_start:]
        if any(name == "abstract" for name, _ in stack):
            abstract_text += text[segment_start:]

    for proof in deferred:
        info = labels.get(proof.labels[0])
        if info and info[2] is not None:
            st = statements[info[2]]
            st.has_proof = True
            st.proof_refs.extend(proof.proof_refs)

    # proofs written as paragraphs: "\emph{Proof of Theorem~\ref{x}.}" outside a proof environment
    for file, start, text in chunks:
        for m in PARAGRAPH_PROOF_RE.finditer(text):
            info = labels.get(m.group(1).strip())
            if info and info[2] is not None and not statements[info[2]].has_proof:
                statements[info[2]].has_proof = True
                find("paragraph_proof", "info", "proof given as a paragraph, not a proof environment; "
                     "its dependencies are not extracted", file, start + text.count("\n", 0, m.start()), m.group(1))

    # an introduction statement followed by "This is Theorem~\ref{x}" is a restatement of x
    for file, start, text in chunks:
        for m in RESTATEMENT_RE.finditer(text):
            before = list(LABEL_RE.finditer(text, max(0, m.start() - 3000), m.start()))
            if not before:
                continue
            info = labels.get(before[-1].group(1).strip())
            target = labels.get(m.group(1).strip())
            if info and info[2] is not None and target and target[2] is not None:
                st = statements[info[2]]
                if not st.has_proof:
                    st.has_proof = True
                    st.restates.append(m.group(1).strip())

    # unresolved references and citations
    for label, file, line, _, _ in refs:
        if label not in labels:
            find("undefined_reference", "error", "reference to an undefined label", file, line, label)
    if bib_sources:
        for key, file, line in cites:
            if key and key not in bib_keys:
                find("undefined_citation", "error", "citation key not found in the bibliography", file, line, key)
    elif cites:
        find("citations_not_checked", "warning", "no .bib file or \\bibitem found; citations not checked",
             str(main), 1)

    # statements without proof
    for st in statements:
        if st.kind in PROOF_KINDS and not st.has_proof and not st.cites_in_statement:
            find("statement_without_proof", "warning",
                 f"{st.kind} has no following proof environment and cites no source", st.file, st.line,
                 st.labels[0] if st.labels else None)

    # dependency graph
    sid_of = {label: info[2] for label, info in labels.items() if info[2] is not None}
    edges: dict[int, set[int]] = {st.sid: set() for st in statements}
    for st in statements:
        own_pos = min((order[l] for l in st.labels), default=None)
        for label in st.restates:   # an introduction restatement points forward by design
            target = sid_of.get(label)
            if target is not None and target != st.sid:
                edges[st.sid].add(target)
        for label in st.proof_refs:
            target = sid_of.get(label)
            if target is None or target == st.sid:
                continue
            edges[st.sid].add(target)
            if own_pos is not None and order.get(label, 0) > own_pos:
                find("forward_reference_in_proof", "warning",
                     "proof cites a result stated later; check that the dependency is acyclic",
                     st.file, st.line, label)
    # cycles (iterative DFS)
    color = {sid: 0 for sid in edges}
    cycles: list[list[int]] = []
    for root in edges:
        if color[root]:
            continue
        stack_dfs: list[tuple[int, list[int]]] = [(root, sorted(edges[root]))]
        path = [root]; color[root] = 1
        while stack_dfs:
            node, todo = stack_dfs[-1]
            if todo:
                nxt = todo.pop()
                if color[nxt] == 1:
                    cycles.append(path[path.index(nxt):] + [nxt])
                elif color[nxt] == 0:
                    color[nxt] = 1; path.append(nxt)
                    stack_dfs.append((nxt, sorted(edges[nxt])))
            else:
                color[node] = 2; path.pop(); stack_dfs.pop()
    name = lambda sid: (statements[sid].labels[0] if statements[sid].labels else f"{statements[sid].kind}@{statements[sid].line}")
    for cycle in cycles:
        st = statements[cycle[0]]
        find("dependency_cycle", "error", "proof dependencies form a cycle: " + " -> ".join(name(s) for s in cycle),
             st.file, st.line)

    # condition propagation
    unproved = {st.sid for st in statements if st.kind in UNPROVED_KINDS}
    closure: dict[int, set[int]] = {}
    def ancestors(sid: int) -> set[int]:
        if sid in closure:
            return closure[sid]
        closure[sid] = set()
        result: set[int] = set()
        for t in edges[sid]:
            result.add(t); result |= ancestors(t)
        closure[sid] = result
        return result
    conditional = []
    for st in statements:
        if st.kind not in PROOF_KINDS:
            continue
        depends = ancestors(st.sid) & unproved
        if not depends:
            continue
        conditional.append(st.sid)
        text = st.text.lower()
        named = any(label in st.text for d in depends for label in statements[d].labels)
        if not named and not any(word in text for word in CONDITION_WORDS):
            find("silent_condition", "error",
                 "statement depends on an unproved node (" + ", ".join(name(d) for d in sorted(depends))
                 + ") but its statement names no condition", st.file, st.line, name(st.sid))
    if conditional and abstract_text and not any(w in abstract_text.lower() for w in CONDITION_WORDS):
        find("abstract_omits_conditions", "warning",
             "some statements are conditional but the abstract mentions no condition", str(main), 1)

    # hand-waving and TODO markers
    for file, start, text in chunks:
        lower = text.lower()
        for phrase in HANDWAVE:
            for m in re.finditer(r"\b" + re.escape(phrase) + r"\b", lower):
                find("handwave_marker", "info", "check this step: a referee will", file,
                     start + text.count("\n", 0, m.start()), phrase)
        for m in TODO_RE.finditer(text):
            find("todo_marker", "warning", "unfinished marker in source", file,
                 start + text.count("\n", 0, m.start()), m.group(0))

    counts = {sev: sum(f["severity"] == sev for f in findings) for sev in ("error", "warning", "info")}
    return {
        "audit": "math-manuscript", "main": str(main), "files": sorted({Path(c[0]).name for c in chunks}),
        "statements": len(statements),
        "by_kind": {k: sum(s.kind == k for s in statements) for k in sorted({s.kind for s in statements})},
        "conditional_statements": [name(s) for s in conditional],
        "dependency_graph": {name(s): sorted(name(t) for t in edges[s]) for s in edges if edges[s]},
        "counts": counts, "findings": findings, "ok": counts["error"] == 0,
        "scope": "structural locator only; it does not verify any proof",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("main", help="main .tex file (\\input files are followed)")
    p.add_argument("--format", choices=("json", "text"), default="json")
    args = p.parse_args(argv)
    path = Path(args.main)
    if not path.is_file():
        print(json.dumps({"audit": "math-manuscript", "error": "cannot read main file"}))
        return 2
    try:
        report = audit(path)
    except (OSError, UnicodeError, RecursionError) as error:
        print(json.dumps({"audit": "math-manuscript", "error": str(error)}))
        return 2
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"{report['statements']} statements; errors {report['counts']['error']}, "
              f"warnings {report['counts']['warning']}, info {report['counts']['info']}")
        for f in report["findings"]:
            if f["severity"] != "info":
                print(f"{f['severity'].upper():7} {f['file']}:{f['line']} {f['code']} {f['token'] or ''} - {f['message']}")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
