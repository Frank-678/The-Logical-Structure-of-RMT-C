#!/usr/bin/env python3
"""运行原有回归并完整保存stdout/stderr/退出码；不启动真实模型或ROS比赛。"""
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
import json
import os
import subprocess
import time

ROOT=Path('/workspace/scratch/457426c876eb')
OUT=ROOT/'review/league/log-upload-20261029/regressions'
OUT.mkdir(exist_ok=True)
json_include=str(ROOT/'review/ros-runtime/include')
commands=[
 ('core',['bash','tests/run.sh']),
 ('scenes',['python3','tests/scenario_test.py','--json-include',json_include]),
 ('oracle',['python3','tests/oracle_test.py','--json-include',json_include]),
 ('practice-tools',['python3','tests/practice_tools_test.py']),
 ('league-65c',['python3','tests/version_league_test.py','--json-include',json_include,'--version','build/league/versions/chatgpt_65c_v2']),
 ('league-8da',['python3','tests/version_league_test.py','--json-include',json_include,'--version','build/league/versions/deepseek_8da_v2'])]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(ROOT/'review/test-deps'),RMTC_JSON_INCLUDE=json_include)
rows=[]
for name,command in commands:
    stamp=datetime.now(ZoneInfo('Asia/Shanghai')).isoformat()
    started=time.monotonic()
    with (OUT/(name+'.stdout.log')).open('w') as stdout,(OUT/(name+'.stderr.log')).open('w') as stderr:
        result=subprocess.run(command,cwd=ROOT/'cst',env=env,stdout=stdout,stderr=stderr)
    row=dict(name=name,command=command,start=stamp,elapsed_seconds=time.monotonic()-started,exit_code=result.returncode)
    rows.append(row)
    (OUT/'receipt.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(row,ensure_ascii=False),flush=True)
raise SystemExit(0 if all(x['exit_code']==0 for x in rows) else 1)
