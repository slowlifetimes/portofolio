"""Revert slider to object-fit: cover approach (gambar full)."""
import re

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# 1. Fix .photo-slider height and background
content = content.replace("height: 460px;", "height: 420px;")
content = content.replace("background: #080b18;", "background: var(--glass-bg);")

# 2. Replace the entire .slider-slide + .slider-bg-blur + .slider-main-img + hover block
old_css = re.search(
    r'(      \.slider-slide \{.*?\.slider-slide:hover \.slider-main-img \{.*?\})',
    content, re.DOTALL
)
if old_css:
    new_css = """      .slider-slide {
        position: relative;
        height: 100%;
        flex-shrink: 0;
        overflow: hidden;
      }

      .slider-slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
      }"""
    content = content[:old_css.start()] + new_css + content[old_css.end():]
    print("CSS replaced successfully")
else:
    print("ERROR: Could not find CSS block to replace")

# 3. Replace slide.innerHTML to simple <img> (remove blur div)
old_js = re.search(
    r"slide\.innerHTML = `\s*<div class=\"slider-bg-blur\".*?`\s*;",
    content, re.DOTALL
)
if old_js:
    new_js = 'slide.innerHTML = `<img src="${encodedSrc}" alt="${f.caption}" loading="lazy"/>`;'
    content = content[:old_js.start()] + new_js + content[old_js.end():]
    print("JS innerHTML replaced successfully")
else:
    print("ERROR: Could not find JS innerHTML block")

# 4. Remove slide.style.flex line
content = re.sub(
    r"\n\s*slide\.style\.flex = .*?;\s*\n",
    "\n",
    content
)
print("Removed slide.style.flex line")

# 5. Fix mobile media query height
content = content.replace(
    ".photo-slider {\n          height: 300px;\n",
    ".photo-slider {\n          height: 260px;\n"
)
# Also try CRLF
content = content.replace(
    ".photo-slider {\r\n          height: 300px;\r\n",
    ".photo-slider {\r\n          height: 260px;\r\n"
)
print("Fixed mobile height")

if content != original:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("\nFile saved successfully!")
else:
    print("\nWARNING: No changes made!")

