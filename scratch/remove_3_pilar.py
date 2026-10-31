with open('model-guru.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '          <span class="sec-tag">3 Pilar Utama</span>\n'
if target in content:
    content = content.replace(target, '')
    print("Removed with \\n")
else:
    target_crlf = '          <span class="sec-tag">3 Pilar Utama</span>\r\n'
    if target_crlf in content:
        content = content.replace(target_crlf, '')
        print("Removed with \\r\\n")
    else:
        # Fallback substring replace
        content = content.replace('<span class="sec-tag">3 Pilar Utama</span>', '')
        print("Removed fallback")

with open('model-guru.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated model-guru.html")

