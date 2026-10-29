import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('../',import.meta.url)).replace(/\/$/,'');
const html=fs.readFileSync(`${root}/materials/addenda/2026-10-25-map-editor/map-editor.html`,'utf8');
const source=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const results=[];
function setup(){
 const elements=new Map();
 const get=id=>{if(!elements.has(id))elements.set(id,{value:id==='zoom'?'28':id==='format'?'geometry':'',style:{},classList:{toggle(){}},options:[],addEventListener(){},getContext(){return{};}});return elements.get(id);};
 const context={document:{getElementById:get,querySelectorAll:()=>[],addEventListener(){}},window:{addEventListener(){}},ResizeObserver:class{observe(){}},requestAnimationFrame:()=>1,console};
 vm.createContext(context);
 const marker='  refresh();\n})();';assert(source.includes(marker));
 vm.runInContext(source.replace(marker,'  globalThis.probe={parseImport,buildOutput,geometry,load:x=>{state=parseImport(x)},format:x=>{$("format").value=x},resize:(w,h)=>{state.width=w;state.height=h}};\n'+marker),context,{timeout:2000});
 return context.probe;
}
const plain=x=>JSON.parse(JSON.stringify(x));
function normalized(x){const v=plain(x);v.map.obstacles.sort((a,b)=>a[1]-b[1]||a[0]-b[0]);v.map.resources.sort((a,b)=>a.position[1]-b.position[1]||a.position[0]-b.position[0]);return v;}
function test(name,f){try{f();results.push({name,status:'pass'});}catch(e){results.push({name,status:'fail',error:e.message});}}
const a=setup();
test('默认geometry仅含map/robots',()=>assert.deepEqual(Object.keys(a.buildOutput()).sort(),['map','robots']));
test('默认24x24且四出生点',()=>{const x=a.buildOutput();assert.equal(x.map.width,24);assert.equal(x.map.height,24);assert.equal(x.robots.length,4)});
let fresh;
test('新建practice默认无任务且关闭事件',()=>{a.format('practice');fresh=plain(a.buildOutput());assert.equal(fresh.stage,2);assert.deepEqual(fresh.missions,[]);assert.deepEqual(fresh.events,{enabled:false});});
for(const stage of [1,2]){
 const cfg=JSON.parse(fs.readFileSync(`${root}/materials/releases/v1.1/practice/rmtc_practice/config/stage${stage}.json`,'utf8'));
 test(`stage${stage}导入导出语义保留，地图数组顺序归一后比较`,()=>{const p=setup();p.load(cfg);p.format('practice');const x=plain(p.buildOutput());assert.deepEqual(normalized(x),normalized(cfg));});
}
const template=JSON.parse(fs.readFileSync(`${root}/materials/releases/v1.1/practice/rmtc_practice/config/stage2.json`,'utf8'));
test('外部event_params_file拒绝',()=>{const p=setup();assert.throws(()=>p.parseImport({...template,event_params_file:'events.json'}));});
test('重复资源ID拒绝',()=>{const p=setup(),x=structuredClone(template);x.map.resources[1].id=x.map.resources[0].id;assert.throws(()=>p.parseImport(x));});
test('越界资源拒绝',()=>{const p=setup(),x=structuredClone(template);x.map.resources[0].position=[999,0];assert.throws(()=>p.parseImport(x));});
test('第二阶段缺席位拒绝',()=>{const p=setup(),x=structuredClone(template);x.robots.pop();assert.throws(()=>p.parseImport(x));});
test('导入后缩图导致reach越界时导出拒绝',()=>{const p=setup();p.load(template);p.format('practice');p.resize(9,9);assert.throws(()=>p.buildOutput());});
test('重绘资源ID稳定且数值保持',()=>{const p=setup();p.load(template);const x=plain(p.geometry());assert.deepEqual(x.map.resources,template.map.resources.slice().sort((a,b)=>a.position[1]-b.position[1]||a.position[0]-b.position[0]));});
test('已知边界：导入允许资源和出生点重叠',()=>{const p=setup(),x=structuredClone(template);x.map.resources[0].position=[...x.robots[0].spawn];assert.doesNotThrow(()=>p.parseImport(x));});
test('已知边界：事件定义坐标未校验',()=>{const p=setup(),x=structuredClone(template);x.events.definitions.pepper.points=[[999,999]];p.load(x);p.format('practice');assert.deepEqual(plain(p.buildOutput()).events.definitions.pepper.points,[[999,999]]);});
const out={source:'EDITOR-01','method':'Node vm执行原始内联JS；注入只读测试入口、最小DOM替身；未修改原件，非浏览器交互测试',results,passed:results.filter(x=>x.status==='pass').length,failed:results.filter(x=>x.status==='fail').length};
fs.writeFileSync(process.argv[2]||`${root}/checks/map-editor-logic.json`,JSON.stringify(out,null,2)+'\n');
if(fresh)fs.writeFileSync(process.argv[3]||`${root}/checks/map-editor-fresh-practice.json`,JSON.stringify(fresh,null,2)+'\n');
console.log(JSON.stringify(out,null,2));
if(out.failed)process.exitCode=1;
