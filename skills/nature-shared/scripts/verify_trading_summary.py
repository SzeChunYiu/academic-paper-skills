#!/usr/bin/env python3
"""Check a normalized equal-panel summary; never certify economic validity."""
import argparse
import json
import math
from pathlib import Path


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ['summary must be an object']
    if data.get('metric') not in ('simple_bp_day', 'log_bp_day', 'geometric_bp_day'):
        errors.append('metric must distinguish simple, log, or geometric bp/day')
    if data.get('aggregation') != 'equal_panel_mean':
        errors.append('unsupported aggregation; panel mean cannot certify a pooled account')
    rows = data.get('panels')
    if not isinstance(rows, list) or not rows:
        return errors + ['panels must be a nonempty list']
    def finite(x):
        return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)
    ids, values = set(), []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f'panel {i} must be an object')
            continue
        ident = row.get('id')
        if not isinstance(ident, str) or not ident.strip():
            errors.append(f'panel {i} needs a nonempty identity')
        elif ident in ids:
            errors.append(f'duplicate panel identity: {ident}')
        else:
            ids.add(ident)
        value = row.get('return')
        if finite(value):
            values.append(value)
        else:
            errors.append(f'panel {i} needs a finite return')
        dd = row.get('max_drawdown_pct')
        if not finite(dd) or not 0 <= dd <= 100:
            errors.append(f'panel {i} needs maximum drawdown as a loss percentage in [0,100]')
    mean = data.get('reported_mean')
    if not finite(mean):
        errors.append('reported_mean must be finite')
    elif len(values) == len(rows) and not math.isclose(sum(values)/len(values), mean, rel_tol=0, abs_tol=.0051):
        errors.append('reported_mean does not match equal-panel arithmetic (0.0051 bp rounding tolerance)')
    claim = data.get('claims_all_positive', False)
    if not isinstance(claim, bool):
        errors.append('claims_all_positive must be boolean')
    elif claim and any(v <= 0 for v in values):
        errors.append('all-positive claim contradicted by a zero or negative panel')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('summary', type=Path)
    args = parser.parse_args()
    try:
        errors = validate(json.loads(args.summary.read_text()))
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({'status': 'FAIL' if errors else 'PASS_REPORTED_ARITHMETIC_ONLY', 'errors': errors}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
