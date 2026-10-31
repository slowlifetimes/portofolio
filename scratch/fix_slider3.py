"""Fix slider: set slide width in pixels for reliable sizing."""

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# 1. In build(), after creating slides, set their width
# Add a function to set slide widths based on slider pixel width
old_build_end = '''          prevBtn.style.display = nextBtn.style.display = "flex";
          dotsWrap.style.display = "flex";
        }'''

new_build_end = '''          prevBtn.style.display = nextBtn.style.display = "flex";
          dotsWrap.style.display = "flex";
          setSlidesWidth();
        }

        function setSlidesWidth() {
          const w = slider.offsetWidth;
          track.querySelectorAll(".slider-slide").forEach(s => {
            s.style.width = w + "px";
          });
        }'''

content = content.replace(old_build_end, new_build_end)

# 2. Update resize handler to also call setSlidesWidth
old_resize = '''        // Recalculate position on resize
        window.addEventListener("resize", () => {
          if (slides.length) {
            const sliderW = slider.offsetWidth;
            track.style.transition = "none";
            track.style.transform = `translateX(-${current * sliderW}px)`;
            requestAnimationFrame(() => {
              track.style.transition = "";
            });
          }
        });'''

new_resize = '''        // Recalculate position on resize
        window.addEventListener("resize", () => {
          if (slides.length) {
            setSlidesWidth();
            const sliderW = slider.offsetWidth;
            track.style.transition = "none";
            track.style.transform = `translateX(-${current * sliderW}px)`;
            requestAnimationFrame(() => {
              track.style.transition = "";
            });
          }
        });'''

content = content.replace(old_resize, new_resize)

if content != original:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Added setSlidesWidth() - pixel-based slide sizing!")
    print("  OK: setSlidesWidth function" if 'function setSlidesWidth' in content else "  FAIL")
    print("  OK: resize calls setSlidesWidth" if 'setSlidesWidth();\n' in content or 'setSlidesWidth();\r\n' in content else "  FAIL")
else:
    print("WARNING: No changes made! Trying CRLF...")
    content = original
    content = content.replace(old_build_end.replace('\n','\r\n'), new_build_end.replace('\n','\r\n'))
    content = content.replace(old_resize.replace('\n','\r\n'), new_resize.replace('\n','\r\n'))
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Fixed with CRLF!")
    else:
        print("Still no changes - need to debug")

