# Verification checker v2: check cited file:line region against evidence fragments.
import json, re, os

REQS = os.environ.get('REQ_JSON', r'D:/code/The-Logical-RMT-C-log/reqs-doc-analysis-a.json')
BASE = os.environ.get('REQ_BASE', r'D:/code/The-Logical-Structure-of-RMT-C/')
WINPREFIX = r'D:/code/The-Logical-Structure-of-RMT-C/'

reqs = json.load(open(REQS, encoding='utf-8'))

MASK_RE = re.compile(r'(?i)(sk-[A-Za-z0-9_\-]{12,})')
TOKEN_RE = re.compile(r'(ai_token\s*=\s*")([^"]{4,})(")')

def mask(s):
    s = MASK_RE.sub('《临时练习密钥》', s)
    s = TOKEN_RE.sub(lambda m: m.group(1) + '《临时练习密钥》' + m.group(3), s)
    return s

def norm(s):
    if s is None:
        return ''
    s = s.replace('\u3000', '')
    for a, b in (('\u201c', '"'), ('\u201d', '"'), ('\u2018', "'"), ('\u2019', "'"),
                 ('\u2014', '-'), ('\u2013', '-'), ('\u00d7', 'x'), ('\uff0c', ','),
                 ('\uff1a', ':'), ('\uff1b', ';'), ('\uff08', '('), ('\uff09', ')'),
                 ('\uff3b', '['), ('\uff3d', ']'), ('\uff0e', '.'), ('\uff1f', '?'),
                 ('\uff01', '!'), ('\u00b7', '-'), ('\uff5c', '|'), ('\u203c', '!!')):
        s = s.replace(a, b)
    return re.sub(r'\s+', '', s)

def fragments(ev):
    return [p for p in re.split(r'\u2026+|\.\.\.+|\|', ev) if len(norm(p)) >= 5]

cache = {}
def readf(rel):
    if rel not in cache:
        p = os.path.join(BASE, rel.replace('/', os.sep))
        try:
            cache[rel] = open(p, encoding='utf-8', errors='replace').read().split('\n')
        except Exception:
            cache[rel] = None
    return cache[rel]

def find_in(frag, nlines):
    nf = norm(frag)
    for i, l in enumerate(nlines, 1):
        if nf in norm(l):
            return i
    return None

out = []
for r in reqs:
    src = r.get('source', '')
    rel, _, cited = src.rpartition(':')
    rel = rel.replace(WINPREFIX, '').replace('\\', '/')
    if ':' in rel:
        rel = re.sub(r'^[A-Za-z]:/', '', rel)
    lines = readf(rel)
    if lines is None:
        out.append((r['id'], 'MISSING_FILE', rel, cited, [], []))
        continue
    try:
        cl = int(cited)
    except ValueError:
        cl = 0
    if cl < 1 or cl > len(lines):
        out.append((r['id'], 'BAD_LINE', rel, cited, [], []))
        continue
    region = lines[max(0, cl - 2): min(len(lines), cl + 8)]
    frags = fragments(r.get('evidence', ''))
    stats = []
    for f in frags:
        rf = find_in(f, region)
        if rf is not None:
            stats.append('R')
        else:
            ff = find_in(f, lines)
            stats.append('F' if ff is not None else 'M')
    out.append((r['id'], 'REG', rel, cited, stats, region))

for rid, kind, rel, cited, stats, region in out:
    if kind == 'REG':
        marks = ' '.join(f'{i+1}:{s}' for i, s in enumerate(stats))
        verdict = 'MET' if all(s == 'R' for s in stats) else ('PART' if 'R' in stats else 'NONE')
        print(f'{rid} | {verdict} | {rel}:{cited} | frags[{marks}]')
        if verdict != 'MET':
            for i, l in enumerate(region, max(1, int(cited) - 2)):
                print(f'    [{i}] {mask(l.strip()[:150])}')
    else:
        print(f'{rid} | {kind} | {rel}:{cited} | {rest if False else ""}')
