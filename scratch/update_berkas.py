with open('berkas.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = 'class="video-action-btn primary" style="display:inline-flex; align-items:center; gap:6px; padding:8px 16px; font-size:0.84rem; text-decoration:none;"'
repl = 'class="video-action-btn primary"'

count = content.count(target)
print(f"Found {count} occurrences in berkas.html")
if count > 0:
    content = content.replace(target, repl)
    with open('berkas.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced successfully in berkas.html")

