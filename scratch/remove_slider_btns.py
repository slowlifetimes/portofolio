"""Remove prev/next buttons from slider — auto-only + dots + swipe."""

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Remove prev/next button HTML
import re
c = re.sub(r'\s*<button\s+class="slider-btn slider-btn-prev".*?</button>', '', c, flags=re.DOTALL)
c = re.sub(r'\s*<button\s+class="slider-btn slider-btn-next".*?</button>', '', c, flags=re.DOTALL)

# 2. Remove JS: btnP/btnN references and event listeners
c = re.sub(r'\s*var btnP\s*=.*?;\s*\n', '\n', c)
c = re.sub(r'\s*var btnN\s*=.*?;\s*\n', '\n', c)
c = re.sub(r'\s*btnP\.addEventListener.*?;\s*\n', '\n', c)
c = re.sub(r'\s*btnN\.addEventListener.*?;\s*\n', '\n', c)
c = re.sub(r'\s*btnP\.style\.display\s*=\s*btnN\.style\.display\s*=\s*"flex";\s*\n', '\n', c)

# In showEmpty, remove btnP/btnN hide
c = re.sub(r'\s*btnP\.style\.display\s*=\s*btnN\.style\.display\s*=\s*"none";\s*\n', '\n', c)

# 3. Remove CSS for .slider-btn
c = re.sub(r'\s*/\* Prev / Next \*/.*?\.slider-btn-next \{[^}]*\}', '', c, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Removed prev/next buttons!")
print(f"  btnP in JS: {'NO' if 'btnP' not in c else 'STILL EXISTS'}")
print(f"  btnN in JS: {'NO' if 'btnN' not in c else 'STILL EXISTS'}")
print(f"  slider-btn CSS: {'NO' if '.slider-btn {' not in c else 'STILL EXISTS'}")
print(f"  sliderPrev HTML: {'NO' if 'sliderPrev' not in c else 'STILL EXISTS'}")

