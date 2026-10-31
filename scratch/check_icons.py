import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.findall(r'data-lucide=[\'"]([^\'"]+)[\'"]', c)
    matches = [x for x in m if any(k in x for k in ['youtube', 'video', 'play'])]
    if matches:
        print(f, set(matches))

