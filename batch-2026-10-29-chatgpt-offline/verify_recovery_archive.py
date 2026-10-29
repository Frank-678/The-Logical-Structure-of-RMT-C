"""保留首次补跑现场；对12份仍截断的回放另开临时目录重跑，校验后把字节写入归档。"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import gzip,hashlib,io,json,sys,tarfile,tempfile
ROOT=Path('/workspace/scratch/457426c876eb');sys.path.insert(0,str(ROOT/'cst/tests'))
import version_league as league,version_store
base=ROOT/'cst/build/league/full-league';recovered=ROOT/'cst/build/league/tape-recovery-20261029';out=ROOT/'review/league/log-upload-20261029'
plan=json.loads((base/'plan.json').read_text());engine=json.loads((base/'engine.json').read_text());binary=ROOT/'cst/build/scenarios'/engine['build_id']/'runner'
assert hashlib.sha256(binary.read_bytes()).hexdigest()==engine['binary_sha256']
versions={label:version_store.load_version(path) for label,path in plan['versions'].items()}
rows=json.loads((out/'recovered-tape-first-audit.json').read_text());receipt=[]
archive=out/'verified-recovery-and-regressions.tar.xz'
with tempfile.TemporaryDirectory(prefix='rmtc-verified-tapes-') as temporary,tarfile.open(archive,'w:xz',preset=3) as tar:
    for row in rows:
        case_id,label,_=Path(row['path']).parts
        folder=recovered/case_id/label
        rerun=False
        if row['error']:
            case=next(c for c in plan['cases'] if c['id']==case_id)
            folder=Path(temporary)/case_id/label
            result=league.play(case,label,plan,versions,binary,engine,folder,5)
            assert result['status']=='passed'
            previous=json.loads((base/case_id/label/'result.json').read_text())
            assert result['world']==previous['world'] and result['result']==previous['result']
            rerun=True
        # 用已读出的原始字节校验并打包，避免校验后再读另一个文件版本。
        original=(folder/'tape.jsonl.gz').read_bytes()
        decoded=gzip.decompress(original)
        records=[json.loads(line) for line in decoded.splitlines()]
        result=json.loads((folder/'result.json').read_text())
        assert [r['tick'] for r in records]==list(range(result['start_tick'],result['end_tick']))
        for p in sorted(folder.iterdir()):
            if not p.is_file():continue
            data=original if p.name=='tape.jsonl.gz' else p.read_bytes()
            info=tarfile.TarInfo(f'verified-recovery/{case_id}/{label}/{p.name}');info.size=len(data);info.mtime=0
            tar.addfile(info,io.BytesIO(data))
        receipt.append(dict(case_id=case_id,label=label,retried_in_temporary=rerun,records=len(records),
                            gzip_sha256=hashlib.sha256(original).hexdigest(),decoded_sha256=hashlib.sha256(decoded).hexdigest(),
                            result_matches_original=result['world']==json.loads((base/case_id/label/'result.json').read_text())['world']))
        print(json.dumps(dict(case_id=case_id,label=label,verified=True,retried=rerun)),flush=True)
    tar.add(out/'regressions',arcname='regressions')
(out/'recovered-tape-integrity.json').write_text(json.dumps(dict(tapes=len(receipt),complete=len(receipt),rows=receipt),ensure_ascii=False,indent=2)+'\n')
# 再从完整归档校验68份回放的原始字节和完整JSONL，而不只检查tar目录。
expected={(r['case_id'],r['label']):r for r in receipt};count=0
with tarfile.open(archive,'r:xz') as tar:
 for member in tar:
  if member.name.endswith('/tape.jsonl.gz'):
   _,case_id,label,_=Path(member.name).parts;raw=tar.extractfile(member).read();item=expected[(case_id,label)]
   assert hashlib.sha256(raw).hexdigest()==item['gzip_sha256'];assert len(gzip.decompress(raw).splitlines())==item['records'];count+=1
assert count==68
print(json.dumps(dict(verified_tapes=count,archive_bytes=archive.stat().st_size,archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest())))
