import os
import json

with open('files/manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Testing manifest foto list:")
missing = 0
for item in data['foto']:
    path = item['src'].replace('/', os.sep)
    exists = os.path.exists(path)
    if not exists:
        print(f"MISSING: {path}")
        missing += 1
    else:
        # print size
        size = os.path.getsize(path)
        # print(f"OK: {path} ({size} bytes)")

print(f"Total in manifest: {len(data['foto'])}, Missing: {missing}")

