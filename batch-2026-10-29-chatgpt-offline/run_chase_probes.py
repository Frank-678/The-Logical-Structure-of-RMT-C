from pathlib import Path
import copy,json,subprocess,sys
ROOT=Path('/workspace/scratch/457426c876eb');out=ROOT/'review/league/log-upload-20261029/chase-probes';(out/'scenes').mkdir(parents=True,exist_ok=True)
base=json.loads((ROOT/'cst/tests/scenarios/attack_before_move.json').read_text())
def script(action,direction=None):
 value={'action':action}
 if direction:value['direction']=direction
 return dict(type='script',event_delivery='oracle',actions={},otherwise=value)
def expect(path,value):return dict(path=path,op='eq',value=value)
def scene(name,cars,agents,until,checks,walls=()):
 s=copy.deepcopy(base);s.update(name=name,map=dict(width=7,height=7,vision_radius=4,walls=list(walls),spawns=[list(cars.get(k,{}).get('position',p)) for k,p in zip('ABCD',[(0,0),(6,0),(0,6),(6,6)])]),initial=dict(tick=200,resources=[],cars=cars),agents=agents,run=dict(until_tick=until,expect=checks))
 return s
corner_cars=dict(A=dict(position=[4,0],hp=100),B=dict(position=[6,0],hp=40))
corner_move=scene('corner-greedy-move-stalls',corner_cars,dict(A=script('move','right'),B=script('move','left')),204,[expect('/world/cars/A/position',[4,0]),expect('/world/cars/B/position',[6,0]),expect('/world/cars/A/D',0),expect('/world/cars/A/invalid',0)])
corner_attack=scene('corner-attack-before-escape',corner_cars,dict(A=script('attack','right'),B=script('move','left')),202,[expect('/world/cars/B/alive',False),expect('/world/cars/A/D',100),expect('/world/cars/A/hp',100)])
corner_current=copy.deepcopy(corner_attack);corner_current['name']='corner-current-strategy-probe';corner_current['agents']['A']=dict(type='strategy',event_delivery='oracle')
reverse=scene('reverse-is-not-a-swap',dict(A=dict(position=[3,3],hp=100),B=dict(position=[4,3],hp=100)),dict(A=script('move','right'),B=script('move','left')),201,[expect('/world/cars/A/position',[3,3]),expect('/world/cars/B/position',[4,3]),expect('/world/cars/A/invalid',0),expect('/world/cars/B/invalid',0)])
car3=dict(A=dict(position=[3,3],hp=30),B=dict(position=[2,3],hp=100),C=dict(position=[4,3],hp=100))
agents=dict(A=script('move','up'),B=script('attack','right'),C=script('attack','left'))
move=scene('two-shooters-move-cancelled',car3,agents,201,[expect('/world/cars/A/alive',False),expect('/world/cars/A/position',[3,3])])
defend=scene('two-shooters-defend-one-tick',car3,{**agents,'A':script('defend')},201,[expect('/world/cars/A/alive',True),expect('/world/cars/A/hp',10)])
wall=scene('wall-does-not-block-normal-attack',dict(A=dict(position=[3,3],hp=100),B=dict(position=[5,3],hp=100)),dict(A=script('attack','right'),B=script('move','up')),201,[expect('/world/cars/B/hp',80),expect('/world/cars/B/position',[5,2])],[[4,3]])
rows=[]
for s in [corner_move,corner_attack,corner_current,reverse,move,defend,wall]:
 path=out/'scenes'/(s['name']+'.json');path.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
 command=[sys.executable,str(ROOT/'cst/tests/run_scenarios.py'),str(path),'--json-include',str(ROOT/'review/ros-runtime/include'),'--out',str(out/s['name'])]
 with (out/(s['name']+'.stdout.log')).open('w') as stdout,(out/(s['name']+'.stderr.log')).open('w') as stderr:
  result=subprocess.run(command,cwd=ROOT/'cst',stdout=stdout,stderr=stderr)
 rows.append(dict(name=s['name'],exit_code=result.returncode,command=command));print(json.dumps(rows[-1]),flush=True)
(out/'receipt.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
raise SystemExit(0 if all(x['exit_code']==0 for x in rows) else 1)
