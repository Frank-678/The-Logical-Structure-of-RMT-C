from pathlib import Path
import sys,json,gzip,tempfile,hashlib
ROOT=Path('/workspace/scratch/457426c876eb');sys.path.insert(0,str(ROOT/'cst/tests'))
import version_league as league,version_store
base=ROOT/'cst/build/league/full-league';plan=json.loads((base/'plan.json').read_text());engine=json.loads((base/'engine.json').read_text());binary=ROOT/'cst/build/scenarios'/engine['build_id']/'runner'
versions={label:version_store.load_version(path) for label,path in plan['versions'].items()}
case=next(c for c in plan['cases'] if c['id']=='asymmetric-C-pressure')
with tempfile.TemporaryDirectory(prefix='rmtc-tape-probe-') as directory:
 p=Path(directory)
 result=league.play(case,'deepseek',plan,versions,binary,engine,p,5)
 tape=p/'tape.jsonl.gz';raw=tape.read_bytes();n=0;error=None
 try:
  with gzip.open(tape,'rt') as stream:
   for line in stream:n+=1
 except Exception as e:error=repr(e)
 record=dict(status=result['status'],end=result.get('end_tick'),bytes=len(raw),last_hex=raw[-12:].hex(),records=n,error=error)
 print(json.dumps(record))
 (ROOT/'review/league/log-upload-20261029/tape-close-probe.json').write_text(json.dumps(record,indent=2)+'\n')
 # 保留原件，即使再次不完整也不补footer伪造。
 import shutil
 shutil.copytree(p,ROOT/'cst/build/league/tape-close-probe')
