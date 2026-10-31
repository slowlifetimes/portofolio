"""Fix slider: simplify to per-slide 100% width approach to avoid fractional rounding bugs."""
import re

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# 1. Fix the build() function:
#    - Remove track.style.width = `${slides.length * 100}%`
#    - Change slide width to just "width: 100%" (100% of the slider, not track)
#    We need each slide to be 100% of the .photo-slider width

# Replace track.style.width line
content = content.replace(
    'track.style.width = `${slides.length * 100}%`;',
    '/* track width is auto via flex */'
)

# Replace slide.style.width line  
content = content.replace(
    'slide.style.width = `${100 / slides.length}%`;',
    '/* slide width set via CSS flex */'
)

# 2. Fix the go() function:
#    Change offset from -(current * (100 / slides.length)) to -(current * 100)
content = content.replace(
    'const offset = -(current * (100 / slides.length));',
    'const offset = -(current * 100);'
)

# 3. Fix CSS: .slider-slide should be width: 100% and flex: 0 0 100%
old_slide_css = """.slider-slide {
        position: relative;
        height: 100%;
        flex-shrink: 0;
        overflow: hidden;
      }"""

new_slide_css = """.slider-slide {
        position: relative;
        height: 100%;
        flex: 0 0 100%;
        width: 100%;
        overflow: hidden;
      }"""

content = content.replace(old_slide_css, new_slide_css)

# Also try CRLF version
old_slide_css_crlf = old_slide_css.replace('\n', '\r\n')
new_slide_css_crlf = new_slide_css.replace('\n', '\r\n')
content = content.replace(old_slide_css_crlf, new_slide_css_crlf)

if content != original:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Slider fixed successfully!")
    
    # Verify
    if 'flex: 0 0 100%' in content:
        print("  - slide flex: 0 0 100% OK")
    if '-(current * 100)' in content:
        print("  - translateX offset OK")
    if 'track width is auto via flex' in content:
        print("  - track width removed OK")
else:
    print("WARNING: No changes made!")

