with open('model-guru.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('            <div class="guru-icon"><i data-lucide="brain"></i></div>\n', '')
content = content.replace('            <div class="guru-icon"><i data-lucide="cpu"></i></div>\n', '')
content = content.replace('            <div class="guru-icon"><i data-lucide="shield-check"></i></div>\n', '')

# Also handle CRLF if needed
content = content.replace('            <div class="guru-icon"><i data-lucide="brain"></i></div>\r\n', '')
content = content.replace('            <div class="guru-icon"><i data-lucide="cpu"></i></div>\r\n', '')
content = content.replace('            <div class="guru-icon"><i data-lucide="shield-check"></i></div>\r\n', '')

with open('model-guru.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Icons removed successfully!")

