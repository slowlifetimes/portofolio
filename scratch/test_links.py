import re, os

with open('berkas.html', 'r', encoding='utf-8') as f:
    c = f.read()

imgs = re.findall(r'<img [^>]*src=[\'"]([^\'"]+)[\'"]', c)
missing_imgs = [src for src in set(imgs) if not os.path.exists(src)]
print('Missing images:', len(missing_imgs), missing_imgs)

links = re.findall(r'href=[\'"](files/dokumen/[^\'"]+)[\'"]', c)
missing_links = [l for l in set(links) if not os.path.exists(l)]
print('Missing doc links:', len(missing_links), missing_links)

