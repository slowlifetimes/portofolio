yt_svg = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" style="vertical-align: middle; margin-right: 4px;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'

for f in ['ppl-mandiri-siklus1.html', 'ppl-mandiri-siklus2.html', 'ppl-mandiri-siklus3.html', 'ppl-mandiri-siklus4.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    target = '<i data-lucide="youtube" style="width: 16px; height: 16px;"></i>'
    if target in c:
        c = c.replace(target, yt_svg)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Replaced youtube icon in {f}")
    else:
        print(f"Target not found in {f}")

