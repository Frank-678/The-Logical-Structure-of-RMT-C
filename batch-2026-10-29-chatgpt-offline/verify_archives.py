from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
for name in ('raw-parts.json','recovery-parts.json', 'first-recovery-parts.json'):
    spec=json.loads((root/name).read_text())
    destination=root/spec['archive']
    with destination.open('wb') as output:
        for item in spec['parts']:
            data=(root/'archives'/item['name']).read_bytes()
            assert len(data)==item['bytes']
            assert hashlib.sha256(data).hexdigest()==item['sha256'],item['name']
            output.write(data)
    assert destination.stat().st_size==spec['bytes']
    assert hashlib.sha256(destination.read_bytes()).hexdigest()==spec['sha256']
    print('verified',destination.name)
