import json, re, os, sys

REPO = r'D:/code/The-Logical-Structure-of-RMT-C'
reqs = json.load(open(r'D:/code/The-Logical-RMT-C-log/reqs-doc-analysis-a.json', encoding='utf-8'))

def norm(s):
    return re.sub(r'\s+', '', s or '')

cache = {}
def readf(path):
    if path not in cache:
        try:
            cache[path] = open(path, encoding='utf-8', errors='replace').read()
        except Exception:
            cache[path] = None
    return cache[path]

def find(req):
    src, _, cited = req['source'].rpartition(':')
    rel = src.replace(REPO + '/', '').replace(REPO + '\\', '')
    p = os.path.join(REPO, rel.replace('/', os.sep))
    txt = readf(p)
    if txt is None:
        return ('FILE_MISSING', rel, cited, '')
    ev = norm(req['evidence'])
    hay = norm(txt)
    kind = 'NONE'
    if ev in hay:
        kind = 'FULL'
    else:
        parts = [norm(x) for x in re.split(r'[;。，：?!]', req['evidence']) if len(norm(x)) >= 6]
        for pt in parts:
            if pt in hay:
                kind = 'PART'
                ev = pt
                break
        if kind == 'NONE' and len(ev) >= 8:
            for i in (0, max(0, len(ev)//2 - 12)):
                sl = ev[i:i+24]
                if len(sl) >= 8 and sl in hay:
                    kind = 'SLICE'
                    ev = sl
                    break
    if kind == 'NONE':
        return ('NOT_FOUND', rel, cited, '')
    lines = txt.split('\n')
    hit = None
    for i, l in enumerate(lines):
        if ev in norm(l):
            hit = i + 1
            break
    return (kind, rel, cited, str(hit) if hit else '?')

import collections
results = []
for r in reqs:
    kind, rel, cited, hit = find(r)
    results.append((r['id'], kind, rel, cited, hit))

c = collections.Counter(x[1] for x in results)
print('summary:', dict(c))
print()
for rid, kind, rel, cited, hit in results:
    if kind != 'FULL':
        print(rid, kind, rel, 'cited:' + cited, 'found:' + hit)

# also print FULL matches that are far from cited line (>4 lines off)
print()
print('line-distance > 4:')
for rid, kind, rel, cited, hit in results:
    if kind == 'FULL' and hit.isdigit() and abs(int(hit) - int(cited)) > 4:
        print(rid, rel, 'cited:' + cited, 'found:' + hit)
