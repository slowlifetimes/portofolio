import json

with open('scratch/verify_curated_34.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('curated_photos = [')
end = text.find(']\n\nprint') + 1
photos_code = text[start + 17:end]
photos = eval(photos_code)

print(f"Applying {len(photos)} curated photos.")

# 1. Update files/manifest.json
with open('files/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

manifest['foto'] = photos

with open('files/manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print("Updated files/manifest.json with 34 photos.")

# 2. Update js/data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

foto_idx = data_js.find('foto: [')
if foto_idx != -1:
    before = data_js[:foto_idx]
    formatted = "foto: [\n"
    for p in photos:
        formatted += f"    {{\n      src: {json.dumps(p['src'])},\n      caption: {json.dumps(p['caption'])},\n      label: {json.dumps(p['label'])},\n    }},\n"
    formatted += "  ],\n};\n"
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(before + formatted)
    print("Updated js/data.js with 34 photos.")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace ALL_WEBSITE_PHOTOS array in index.html
start_marker = 'const ALL_WEBSITE_PHOTOS = ['
end_marker = '];\n        const track = document.getElementById("sliderTrack");'
if end_marker not in idx_content:
    end_marker = '];\r\n        const track = document.getElementById("sliderTrack");'

s_pos = idx_content.find(start_marker)
e_pos = idx_content.find(end_marker)

if s_pos != -1 and e_pos != -1:
    new_array_code = "const ALL_WEBSITE_PHOTOS = " + json.dumps(photos, indent=10, ensure_ascii=False)
    idx_content = idx_content[:s_pos] + new_array_code + idx_content[e_pos + 1:]
    print("Replaced ALL_WEBSITE_PHOTOS in index.html")
else:
    print("Markers not found in index.html!", s_pos, e_pos)

# Update version query parameter
idx_content = idx_content.replace('js/data.js?v=20261031_03', 'js/data.js?v=20261031_04')
idx_content = idx_content.replace('js/main.js?v=20261031_03', 'js/main.js?v=20261031_04')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("Finished updating index.html with curated 34 photos.")

