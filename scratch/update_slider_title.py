with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_title = 'Momen PPL Terbimbing'
new_title = 'Dokumentasi Kegiatan PPL'

content = content.replace(old_title, new_title)
print(f"Replaced title: '{old_title}' -> '{new_title}'")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")

