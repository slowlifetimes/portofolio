import json

with open('files/manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, p in enumerate(data['foto']):
    print(f"{i+1}. [{p['label']}] {p['caption']} -> {p['src']}")

