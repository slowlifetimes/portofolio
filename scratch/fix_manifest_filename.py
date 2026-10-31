import json

with open('files/manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix the berkas.dokumentasi entry with wrong filename
for doc in data.get('berkas', {}).get('dokumentasi', []):
    if 'and dosen' in doc.get('filename', ''):
        old = doc['filename']
        doc['filename'] = doc['filename'].replace('and dosen', 'dan dosen')
        print(f"Fixed: '{old}' -> '{doc['filename']}'")

with open('files/manifest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done!")

