#!/usr/bin/env python3
"""Validate authored relative Markdown targets; leave original archives unchanged."""
from pathlib import Path
import json,re
from urllib.parse import unquote,urlsplit
root=Path(__file__).resolve().parents[1]
errors=[]; checked=0
for p in root.rglob('*.md'):
    rel=p.relative_to(root)
    if rel.parts[0]=='upstream':continue
    if rel.parts[0]=='materials' and rel.parts[1] not in ('addenda','README.md'):continue
    body=re.sub(r'```.*?```|~~~.*?~~~','',p.read_text(),flags=re.S)
    for match in re.finditer(r'!?\[[^\]]*\]\(([^\s]+?)(?:\s+"[^"]*")?\)',body):
        target=match[1].strip('<>');url=urlsplit(target)
        if url.scheme or target.startswith('#'):continue
        checked+=1
        dest=(p.parent/unquote(url.path)).resolve()
        if not dest.exists():errors.append({'file':str(rel),'target':target})
print(json.dumps({'relative_links_checked':checked,'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
