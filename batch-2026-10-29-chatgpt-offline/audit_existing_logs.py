#!/usr/bin/env python3
"""只读检查现存回放完整性；截断原件照样归档，不补造Tick或覆盖旧结果。"""
from pathlib import Path
import gzip
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/457426c876eb')
BASE = ROOT / 'cst/build/league/full-league'
rows, secret_hits = [], []
key = re.compile(rb'sk-[A-Za-z0-9_-]{20,}')
for path in sorted(BASE.rglob('tape.jsonl.gz')):
    result_path = path.parent / 'result.json'
    result = json.loads(result_path.read_text())
    ticks, error, digest = [], None, hashlib.sha256()
    try:
        with gzip.open(path, 'rb') as stream:
            for line in stream:
                digest.update(line)
                if key.search(line): secret_hits.append(str(path.relative_to(BASE)))
                ticks.append(json.loads(line)['tick'])
    except (EOFError, OSError, ValueError, KeyError) as exc:
        error = f'{type(exc).__name__}: {exc}'
    expected = result.get('end_tick', 0) - result.get('start_tick', 0)
    contiguous = ticks == list(range(result.get('start_tick', 0), result.get('end_tick', 0)))
    rows.append(dict(path=str(path.relative_to(BASE)), source_result_status=result['status'],
                     start_tick=result.get('start_tick'), end_tick=result.get('end_tick'),
                     expected_records=expected, decoded_records=len(ticks), first_tick=ticks[0] if ticks else None,
                     last_tick=ticks[-1] if ticks else None, gzip_complete=error is None, error=error,
                     expected_ticks_complete=contiguous, decoded_prefix_sha256=digest.hexdigest(),
                     raw_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
for path in BASE.rglob('*'):
    if path.is_file() and path.suffix != '.gz' and key.search(path.read_bytes()):
        secret_hits.append(str(path.relative_to(BASE)))
summary = dict(scope='read-only integrity audit of preserved local artifacts; not a new game run',
               tapes=len(rows), gzip_complete=sum(x['gzip_complete'] for x in rows),
               expected_ticks_complete=sum(x['expected_ticks_complete'] for x in rows),
               incomplete=sum(not (x['gzip_complete'] and x['expected_ticks_complete']) for x in rows),
               secret_shape_files=sorted(set(secret_hits)), rows=rows)
out=ROOT/'review/league/log-upload-20261029/old-tape-integrity.json'
out.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},ensure_ascii=False))
