import urllib.request
import json
import re

# Fetch lucide icon list or inspect lucide.min.js
url = "https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
    print(f"Downloaded lucide bundle ({len(content)} bytes)")
    
    with open('berkas.html', 'r', encoding='utf-8') as f:
        berkas_html = f.read()

    used_icons = set(re.findall(r'data-lucide=[\'"]([^\'"]+)[\'"]', berkas_html))
    print(f"Icons used in berkas.html ({len(used_icons)}):", used_icons)

    missing = []
    for icon in used_icons:
        # Check if icon name exists as property in lucide
        # In lucide umd, icon names are camelCase or kebab-case keys
        camel = re.sub(r'-([a-z0-9])', lambda m: m.group(1).upper(), icon)
        if f'"{camel}"' not in content and f'"{icon}"' not in content and f'{camel}:' not in content:
            missing.append(icon)

    print("Missing icons in Lucide bundle:", missing)
except Exception as e:
    print("Error:", e)

