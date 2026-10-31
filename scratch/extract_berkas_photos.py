import re

with open('berkas.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find cards
cards = re.findall(r'<div class="photo-card-glass[^"]*".*?</div>\s*</div>\s*</div>', html, re.DOTALL)
print(f"Cards found via regex: {len(cards)}")

# Or search all img src in #photoGalleryGrid
gallery_match = re.search(r'<div class="photo-gallery-grid" id="photoGalleryGrid">(.*?)</div>\s*</div>\s*</section>', html, re.DOTALL)
if gallery_match:
    grid_html = gallery_match.group(1)
    imgs = re.findall(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"', grid_html)
    print(f"Found {len(imgs)} images in photoGalleryGrid:")
    for src, alt in imgs:
        print(f"  {src} -> {alt}")
else:
    print("photoGalleryGrid not matched")

