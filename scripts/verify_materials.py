#!/usr/bin/env python3
"""Read-only checks of archived inputs and the original practice manifest."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((root / 'materials/catalog.json').read_text())
for item in catalog:
    p = root / item['path']
    if not p.is_file():
        errors.append('missing: ' + item['path'])
    elif item.get('sha256') and hashlib.sha256(p.read_bytes()).hexdigest() != item['sha256']:
        errors.append('digest: ' + item['path'])
kit = root / 'materials/practice/rmtc_practice'
manifest = json.loads((kit / 'manifest.json').read_text())
for name, expected in manifest['files'].items():
    p = kit / name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
        errors.append('practice digest: ' + name)
print(json.dumps({'original_attachments': 8, 'catalog_entries': len(catalog),
                  'practice_files_checked': len(manifest['files']),
                  'errors': errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
