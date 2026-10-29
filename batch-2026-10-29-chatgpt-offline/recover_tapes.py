#!/usr/bin/env python3
"""原engine/原冻结worker补跑68条不完整回放；新目录，旧原件不改。"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
import sys
import time

ROOT=Path('/workspace/scratch/457426c876eb')
sys.path.insert(0,str(ROOT/'cst/tests'))
import version_league as league
import version_store

BASE=ROOT/'cst/build/league/full-league'
OUT=ROOT/'cst/build/league/tape-recovery-20261029'
OUT.mkdir(exist_ok=True)
plan=json.loads((BASE/'plan.json').read_text())
engine=json.loads((BASE/'engine.json').read_text())
binary=ROOT/'cst/build/scenarios'/engine['build_id']/'runner'
if hashlib.sha256(binary.read_bytes()).hexdigest()!=engine['binary_sha256']:
    raise SystemExit('original engine binary does not match archived identity')
versions={label:version_store.load_version(path) for label,path in plan['versions'].items()}
manifest=json.loads((ROOT/'review/league/log-upload-20261029/old-tape-integrity.json').read_text())
rows=[]
(OUT/'engine.json').write_text(json.dumps(engine,ensure_ascii=False,indent=2)+'\n')
(OUT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
(OUT/'versions.json').write_text((BASE/'versions.json').read_text())
for item in manifest['rows']:
    if item['gzip_complete'] and item['expected_ticks_complete']:
        continue
    case_id,label,_=Path(item['path']).parts
    case=next(case for case in plan['cases'] if case['id']==case_id)
    started=time.monotonic()
    report=league.play(case,label,plan,versions,binary,engine,OUT/case_id/label,5)
    previous=json.loads((BASE/case_id/label/'result.json').read_text())
    comparison={field:report.get(field)==previous.get(field) for field in ('world','result','rank','win_share','stationary_windows','event_observations')}
    row=dict(case_id=case_id,label=label,status=report['status'],matches=comparison,
             elapsed_seconds=time.monotonic()-started,at=datetime.now(ZoneInfo('Asia/Shanghai')).isoformat())
    rows.append(row)
    (OUT/'recovery-receipt.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(row,ensure_ascii=False),flush=True)
print(json.dumps(dict(completed=len(rows),failures=sum(x['status']!='passed' for x in rows),different=sum(not all(x['matches'].values()) for x in rows)),ensure_ascii=False))
raise SystemExit(0 if all(x['status']=='passed' for x in rows) else 1)
