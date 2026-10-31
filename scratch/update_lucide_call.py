with open('ppl-mandiri.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '          buildToc(targetId);\n          if (targetId === \'tab-non-mengajar\''
replacement = '          buildToc(targetId);\n          if (window.lucide) lucide.createIcons();\n          if (targetId === \'tab-non-mengajar\''

if target in c:
    c = c.replace(target, replacement, 1)
    with open('ppl-mandiri.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Successfully added lucide.createIcons() on tab switch")
else:
    print("Target not found")

