import os
import hashlib

all_files = []
for root, dirs, files in os.walk('files/foto'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            path = os.path.join(root, f)
            all_files.append(path)

hashes = {}
duplicates = []
for p in all_files:
    with open(p, 'rb') as fp:
        md5 = hashlib.md5(fp.read()).hexdigest()
    if md5 in hashes:
        duplicates.append((p, hashes[md5]))
    else:
        hashes[md5] = p

print(f"Total image files scanned: {len(all_files)}")
print(f"Duplicates found: {len(duplicates)}")
for dup, orig in duplicates:
    print(f"  DUPLICATE: {dup}\n    ORIGINAL: {orig}\n")

