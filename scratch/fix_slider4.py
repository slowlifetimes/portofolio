"""Move slider variable declaration to top and remove duplicate."""

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# 1. Add slider declaration right after track declaration
content = content.replace(
    'const track = document.getElementById("sliderTrack");',
    'const slider = document.getElementById("photoSlider");\r\n        const track = document.getElementById("sliderTrack");'
)

# 2. Remove the duplicate slider declaration further down
content = content.replace(
    '\r\n        const slider = document.getElementById("photoSlider");\r\n        slider.addEventListener(',
    '\r\n        slider.addEventListener('
)

# Also handle LF-only
if content == original:
    content = original.replace(
        'const track = document.getElementById("sliderTrack");',
        'const slider = document.getElementById("photoSlider");\n        const track = document.getElementById("sliderTrack");'
    )
    content = content.replace(
        '\n        const slider = document.getElementById("photoSlider");\n        slider.addEventListener(',
        '\n        slider.addEventListener('
    )

if content != original:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Verify no duplicate
    c = content.count('const slider = document.getElementById("photoSlider")')
    print(f"slider declarations: {c} (should be 1)")
    print("Fixed!" if c == 1 else "WARNING: duplicate still exists")
else:
    print("No changes made")

