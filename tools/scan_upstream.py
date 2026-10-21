from pathlib import Path
from collections import Counter, defaultdict
import ast, csv, gzip, hashlib, io, json, re, subprocess

import argparse
ap=argparse.ArgumentParser()
ap.add_argument('--upstream',type=Path,default=Path(__file__).resolve().parents[1]/'upstream/meow-ai-arena')
ap.add_argument('--out',type=Path,required=True)
args=ap.parse_args()
ROOT=args.upstream.resolve()
OUT=args.out.resolve()
OUT.mkdir(parents=True, exist_ok=True)
PATHS = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().rstrip('\0').split('\0')
rows = []
errors = []
symbols = {}
duplicates = defaultdict(list)

def shape(value):
    if isinstance(value, dict):
        return {'type':'object', 'keys':list(value)[:40], 'items':len(value)}
    if isinstance(value, list):
        return {'type':'array', 'items':len(value), 'first':shape(value[0]) if value else None}
    return {'type':type(value).__name__}

def consume_jsonl(stream):
    n=0; first=None; last=None; key_counts=Counter(); fault_counts=Counter()
    for line in stream:
        if not line.strip(): continue
        v=json.loads(line)
        if first is None:first=shape(v)
        last=shape(v);n+=1
        if isinstance(v,dict):
            key_counts.update(v.keys())
            for k in ['reason','error','fault','status']:
                if k in v and isinstance(v[k],(str,int,bool)):fault_counts[f'{k}={v[k]}']+=1
    return {'records':n,'first':first,'last':last,'keys':dict(key_counts),'status_counts':dict(fault_counts)}

for name in PATHS:
    p=ROOT/name; data=p.read_bytes(); digest=hashlib.sha256(data).hexdigest(); duplicates[digest].append(name)
    row={'path':name,'bytes':len(data),'sha256':digest,'read':'complete_bytes','group':name.split('/')[0] if '/' in name else '(root)'}
    try:
        if p.suffix=='.gz':
            with gzip.open(p,'rt',encoding='utf-8-sig') as f:
                if p.name.endswith('.jsonl.gz'):row['data']=consume_jsonl(f)
                else:row['data']=shape(json.load(f))
            row['read']='complete_gzip_decoded_and_json_parsed'
        else:
            text=data.decode('utf-8-sig');row['lines']=len(text.splitlines());row['characters']=len(text)
            if p.suffix=='.json':row['data']=shape(json.loads(text));row['read']='complete_json_parsed'
            elif p.suffix=='.jsonl':row['data']=consume_jsonl(io.StringIO(text));row['read']='complete_jsonl_parsed'
            elif p.suffix=='.csv':
                records=list(csv.reader(io.StringIO(text)));row['data']={'records':len(records)-1,'header':records[0] if records else []};row['read']='complete_csv_parsed'
            elif p.suffix=='.py':
                tree=ast.parse(text);syms=[]
                for node in ast.walk(tree):
                    if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
                        syms.append({'name':node.name,'line':node.lineno,'end':node.end_lineno,'type':type(node).__name__,'doc':ast.get_docstring(node)})
                symbols[name]=sorted(syms,key=lambda x:x['line']);row['read']='complete_text_and_python_AST'
            elif p.suffix in ['.cpp','.h','.hpp']:
                syms=[]
                for i,line in enumerate(text.splitlines(),1):
                    if re.match(r'\s*(?:class|struct)\s+\w+',line) or re.match(r'\s*(?:[\w:<>,*&~]+\s+)+[\w:~]+\([^;]*\)\s*(?:const\s*)?(?:noexcept\s*)?\{',line):
                        syms.append({'line':i,'signature':line.strip()[:240]})
                symbols[name]=syms;row['read']='complete_text_and_symbol_index'
            elif p.suffix=='.md':row['headings']=re.findall(r'^#{1,6}\s+.+$',text,re.M);row['read']='complete_markdown_text'
            elif p.suffix=='.html':
                scripts=re.findall(r'<script[^>]*>(.*?)</script>',text,re.S|re.I);row['scripts']=len(scripts);row['script_characters']=sum(map(len,scripts));embedded=[]
                for script in scripts:
                    for m in re.finditer(r'\b(?:const|let|var)\s+(\w+)\s*=\s*(?=[\[{])',script):
                        try:
                            value,end=json.JSONDecoder().raw_decode(script[m.end():]);entry={'name':m.group(1),**shape(value)}
                            if isinstance(value,dict):entry['arrays']={k:len(v) for k,v in value.items() if isinstance(v,list)}
                            embedded.append(entry)
                        except (ValueError,TypeError):pass
                row['embedded_json']=embedded;row['read']='complete_html_scripts_scanned_embedded_JSON_parsed'
            else:row['read']='complete_utf8_text'
    except Exception as e:
        row['parse_error']=f'{type(e).__name__}: {e}';errors.append({'path':name,'error':row['parse_error']})
    rows.append(row)

(OUT/'inventory.json').write_text(json.dumps({'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'files':rows,'errors':errors},ensure_ascii=False,indent=2))
(OUT/'symbols.json').write_text(json.dumps(symbols,ensure_ascii=False,indent=2))
(OUT/'duplicates.json').write_text(json.dumps({k:v for k,v in duplicates.items() if len(v)>1},ensure_ascii=False,indent=2))
summary={'files':len(rows),'bytes':sum(x['bytes'] for x in rows),'unique_contents':len(duplicates),'read_modes':dict(Counter(x['read'] for x in rows)),'parse_errors':errors,'archives':[{k:r[k] for k in ['path','bytes','data'] if k in r} for r in rows if r['path'].endswith('.gz')]}
(OUT/'scan_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print(json.dumps(summary,ensure_ascii=False,indent=2))
