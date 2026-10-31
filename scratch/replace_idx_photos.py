import json

with open('scratch/verify_curated_34.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('curated_photos = [')
end = text.find(']\n\nprint') + 1
photos = eval(text[start + 17:end])

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = 'const ALL_WEBSITE_PHOTOS = ['
end_marker = '];\n\n        const track = document.getElementById("sliderTrack");'
if end_marker not in content:
    end_marker = '];\r\n\r\n        const track = document.getElementById("sliderTrack");'

s_pos = content.find(start_marker)
e_pos = content.find(end_marker)

print("Found markers:", s_pos, e_pos)
new_code = "const ALL_WEBSITE_PHOTOS = " + json.dumps(photos, indent=10, ensure_ascii=False) + ";\n\n        const track = document.getElementById(\"sliderTrack\");"

content = content[:s_pos] + new_code + content[e_pos + len(end_marker):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")

