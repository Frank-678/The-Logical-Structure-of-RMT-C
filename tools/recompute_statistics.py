#!/usr/bin/env python3
"""Recompute selected published-data invariants; never starts a game or model."""
from pathlib import Path
import argparse
from collections import Counter
import gzip
import importlib.util
import json

here = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument('--upstream', type=Path, default=here / 'upstream/meow-ai-arena')
args = ap.parse_args()
up = args.upstream
def records(name):
    with gzip.open(up / name, 'rt', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]
rows = records('ctf/results/games.jsonl.gz')
spec = importlib.util.spec_from_file_location('meow_bt', up / 'arena/bt.py')
bt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bt)  # Pure rating code at the verified fixed commit.
reference = json.loads((up / 'ctf/results/ratings.json').read_text())['ratings']
fit = bt.fit(rows, sorted(reference), '基准')
out = {'ctf': {'rows': len(rows), 'unique_ids': len({r['id'] for r in rows}),
               'score_equals_captures': all(r['score'][i] == s.get('captures', 0)
                  for r in rows for i, s in enumerate(r['stats'])),
               'fault_counts': sum(sum(r['faults'].values()) for r in rows),
               'rating_point_max_error': max(abs(fit[n] - reference[n][0]) for n in reference)}}
out['land'] = {'modes': dict(Counter(r['mode'] for r in records('land/results/games.jsonl.gz')))}
for n in [1, 2, 3]:
    d = json.loads((up / f'diplomacy/games/game{n}/state.json').read_text())
    result = d['result']
    counts = {p: len(c) for p, c in result['centers'].items()}
    total = sum(v * v for v in counts.values()) or 1
    expected = {p: (100.0 if p in result['winners'] else 0.0) if result['type'] == 'solo'
                else round(100 * v * v / total, 2) for p, v in counts.items()}
    out[f'diplomacy{n}'] = {'phases': len(d['history']), 'messages': len(d['messages']),
                             'score_matches': expected == result['scores']}
teams = json.loads((up / 'warehouse/results/团队成绩.json').read_text())['teams']
weights = dict(S1=.15, D=.10, M1=.05, A=.20, C=.20, S2=.20, M2=.10)
out['warehouse'] = {'all_within_rounding': all(abs(sum(r[k] * w for k, w in weights.items())
                                       - r['team_total']) < .02 for r in teams.values())}
print(json.dumps(out, ensure_ascii=False, indent=2))
assert out['ctf']['rating_point_max_error'] < 1e-8
assert out['ctf']['score_equals_captures']
assert all(out[f'diplomacy{n}']['score_matches'] for n in [1, 2, 3])
assert out['warehouse']['all_within_rounding']
