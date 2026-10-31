import re
import json

with open('berkas.html', 'r', encoding='utf-8') as f:
    berkas_html = f.read()

# Find all img src in berkas.html
berkas_imgs = re.findall(r'<img\s+src="([^"]+)"', berkas_html)
unique_berkas = set(berkas_imgs)
print(f"Total unique images in berkas.html: {len(unique_berkas)}")

with open('files/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

manifest_srcs = {p['src'] for p in manifest['foto']}
print(f"Total images in manifest.foto: {len(manifest_srcs)}")

# Compare
not_in_manifest = unique_berkas - manifest_srcs
print(f"In berkas.html but NOT in manifest.foto: {len(not_in_manifest)}")
for img in sorted(not_in_manifest):
    print("  Missing from manifest:", img)

