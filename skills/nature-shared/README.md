# `nature-shared/` - academic-paper 技能的共享支持包

这个目录是一个可安装但不应单独触发的支持包。它保存 canonical academic-paper 与兼容 `nature-*` 技能共同依赖的公共定义与参考材料，避免在不同技能目录中重复维护同一套内容。安装整套技能时，它会与其他技能一起被发现和更新。

同级技能会通过 `manifest.yaml` 中的相对路径引用这里的文件，例如：

```yaml
always_load:
  - ../nature-shared/core/reader-workflow.md
```

## 当前内容

| 文件 | 使用方 |
|---|---|
| `core/reader-workflow.md` | `nature-polishing`, `nature-writing` |
| `core/paper-type-taxonomy.md` | `nature-polishing`, `nature-writing` |
| `core/ethics.md` | `nature-polishing`, `nature-writing` |
| `core/research-compliance.md` | `nature-writing` 及需要 Nature Portfolio 专项合规检查的技能 |
| `core/atomic-claim-verification.md` | `academic-writing`, `academic-paper-pipeline`, `nature-writing`, `nature-reviewer`, `nature-polishing`, `nature-response` |
| `core/study-protocol-conduct-contract.md` | `academic-writing`, `academic-paper-pipeline` |
| `core/data-integrity-stewardship-contract.md` | `academic-writing`, `academic-paper-pipeline` 与下游 data/figure/review workflows |
| `data-contracts/` + `scripts/resolve_data_integrity.py` | machine-readable data lifecycle、non-universal adapters、evidence provenance 与 bounded evaluation |
| `core/statistical-inference-uncertainty-contract.md` | `academic-writing`、`academic-paper-pipeline`、`nature-statistics` 与下游 display/review workflows |
| `analysis-contracts/` + `scripts/resolve_statistical_inference.py` | machine-readable estimand/execution/uncertainty/surface lifecycle、composable non-universal adapters、time-versioned evidence 与 bounded evaluation |
| `core/terminology-ledger.md` | `nature-polishing`, `nature-writing`, `nature-reader`, `nature-paper2ppt` |
| `core/consistency-sweep.md` | `nature-polishing`, `nature-reviewer`, `nature-response`, `nature-statistics` |
| `core/main-text-discipline.md` | `nature-writing`, `nature-polishing`, `nature-response` |
| `journal-formats/nat-comms.md` | `nature-polishing`, `nature-writing` |
| `journal-formats/nature.md` | `nature-writing` 及需要旗舰 `Nature Article` 精确投稿规则的技能 |
| `journal-formats/nature-machine-intelligence.md` | NMI 投稿的写作、润色、图表、数据与统计工作流 |

`core/atomic-claim-verification.md` 是失效即关闭（fail-closed）的科学内容核查契约。全文、形式化主张和投稿就绪工作流必须枚举每个原子内容项，核查所指证据是否真正蕴含该项；只要仍有 `SUPPORTED_INTERNAL`、`UNRESOLVED`、`CONTRADICTED`、`BLOCKED` 或 `NOT_ASSESSABLE` 项，就不得判定为“核查完整且已就绪”。

`core/data-integrity-stewardship-contract.md` 保存从 source/acquisition
record，经 immutable raw 或 exact external-reference origin、validated 与 analysis-ready snapshots、QC 和
transformation receipts、analysis/display inputs、governance 到 release 的 authority
chain。Maintained adapters 明确是 non-universal；unmatched modality 与 exact
institution、law、funder、repository、licence、consent 或 community policy 必须走
live competent-source resolution。通过 bounded checks 不证明 accuracy、
completeness、representativeness、privacy、legal compliance、reproducibility、
scientific truth 或 acceptance。

`core/statistical-inference-uncertainty-contract.md` 保存从 question 与 estimand，
经 independent unit/dependence、analysis population、plan、immutable input、
execution、diagnostics/sensitivity、typed uncertainty，以及每个
table/display/caption/prose binding，到 bounded claim 的 authority chain。其
maintained adapters 只返回 applicable obligations，不选择 universal best test、
model、prior、interval、threshold 或 frequentist template。Unmatched domain 与
exact regulator/venue rule 必须走 live、date-aware source resolution。通过不证明
model adequacy、causal identification、adequate precision、external validity、
scientific truth 或 acceptance。

`scripts/check_consistency.py` 为一致性扫描提供机械初筛，可报告术语变体、同值不同精度和等值长度单位混用。`scripts/audit_manuscript_surface.py` 补充面向目标期刊的摘要、术语、占位符与渲染表面诊断。脚本输出只用于分诊，不能代替原子核查台账。

## 什么时候把文件放到这里

只有当**两个或更多技能**需要复用同一份内容时，才把文件放入 `nature-shared/`。如果内容只服务于一个技能，应保留在该技能自己的 `static/` 或 `references/` 目录中。

## 什么时候保持技能内局部内容

共享层只放**定义和参考材料**，例如论文类型分类、读者工作流、伦理规则或术语表。具体技能如何诊断、起草、修改或输出结果，仍应保留在各自的 `static/fragments/` 中。多个技能可以复用同一套论文类型分类，但在其上执行不同的任务逻辑。

## 与其它技能的关系

`nature-shared/` 不是独立工作流，而是被 canonical 与兼容 academic-paper 技能按需读取的公共依赖包。
