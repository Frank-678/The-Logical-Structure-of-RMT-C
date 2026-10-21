#!/usr/bin/env python3
"""Verify the fixed submodule, all recorded source hashes, and exact excerpts."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument('--upstream', type=Path, default=root / 'upstream/meow-ai-arena')
args = ap.parse_args()
lock = json.loads((root / 'sources.lock.json').read_text())['upstreams'][0]
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=args.upstream, text=True).strip()
errors = []
if head != lock['commit']:
    errors.append('upstream HEAD differs from pinned commit')
inventory = json.loads((root / 'indexes/upstream-inventory.json').read_text())['files']
for item in inventory:
    p = args.upstream / item['path']
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != item['sha256']:
        errors.append('upstream digest: ' + item['path'])
snippets = json.loads((root / 'snippets/manifest.json').read_text())
for item in snippets:
    source = (args.upstream / item['source_path']).read_text().splitlines(keepends=True)
    body = ''.join(source[item['start_line'] - 1:item['end_line']])
    copied = ''.join((root / item['path']).read_text().splitlines(keepends=True)[item['header_lines']:])
    if body != copied or hashlib.sha256(body.encode()).hexdigest() != item['excerpt_sha256']:
        errors.append('excerpt mismatch: ' + item['path'])
print(json.dumps({'commit': head, 'source_files_checked': len(inventory),
                  'snippets_checked': len(snippets), 'errors': errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
