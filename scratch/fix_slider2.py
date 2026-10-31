"""Fix slider: use pixel-based translateX for reliable positioning."""

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# ── 1. Replace the build() and go() functions ──
old_build_go = '''        function build() {
          track.innerHTML = "";
          dotsWrap.innerHTML = "";

          /* track width is auto via flex */

          slides.forEach((f, i) => {
            const slide = document.createElement("div");
            slide.className = "slider-slide";
            /* slide width set via CSS flex */
            const encodedSrc = encodeURI(f.src);
            slide.innerHTML = `<img src="${encodedSrc}" alt="${f.caption}" loading="lazy"/>`;
            track.appendChild(slide);

            const dot = document.createElement("button");
            dot.className = "slider-dot";
            dot.setAttribute("aria-label", `Foto ${i + 1}`);
            dot.addEventListener("click", () => {
              go(i);
              resetAuto();
            });
            dotsWrap.appendChild(dot);
          });

          prevBtn.style.display = nextBtn.style.display = "flex";
          dotsWrap.style.display = "flex";
        }

        function go(idx) {
          current = (idx + slides.length) % slides.length;
          const offset = -(current * 100);
          track.style.transform = `translateX(${offset}%)`;'''

new_build_go = '''        function build() {
          track.innerHTML = "";
          dotsWrap.innerHTML = "";

          slides.forEach((f, i) => {
            const slide = document.createElement("div");
            slide.className = "slider-slide";
            const encodedSrc = encodeURI(f.src);
            slide.innerHTML = `<img src="${encodedSrc}" alt="${f.caption}" loading="lazy"/>`;
            track.appendChild(slide);

            const dot = document.createElement("button");
            dot.className = "slider-dot";
            dot.setAttribute("aria-label", `Foto ${i + 1}`);
            dot.addEventListener("click", () => {
              go(i);
              resetAuto();
            });
            dotsWrap.appendChild(dot);
          });

          prevBtn.style.display = nextBtn.style.display = "flex";
          dotsWrap.style.display = "flex";
        }

        function go(idx) {
          current = (idx + slides.length) % slides.length;
          const sliderW = slider.offsetWidth;
          track.style.transform = `translateX(-${current * sliderW}px)`;'''

content = content.replace(old_build_go, new_build_go)

# Also try CRLF version
if old_build_go not in original:
    old_crlf = old_build_go.replace('\n', '\r\n')
    new_crlf = new_build_go.replace('\n', '\r\n')
    content = original.replace(old_crlf, new_crlf)

# ── 2. Add window resize handler (before the initSlider call) ──
# Find initSlider() call and add resize listener before it
old_init = '        initSlider();'
new_init = '''        // Recalculate position on resize
        window.addEventListener("resize", () => {
          if (slides.length) {
            const sliderW = slider.offsetWidth;
            track.style.transition = "none";
            track.style.transform = `translateX(-${current * sliderW}px)`;
            requestAnimationFrame(() => {
              track.style.transition = "";
            });
          }
        });

        initSlider();'''

content = content.replace(old_init, new_init)

# ── 3. Fix CSS: slider-slide should use min-width ──
old_css = '''.slider-slide {
        position: relative;
        height: 100%;
        flex: 0 0 100%;
        width: 100%;
        overflow: hidden;
      }'''

new_css = '''.slider-slide {
        position: relative;
        height: 100%;
        flex-shrink: 0;
        overflow: hidden;
      }'''

content = content.replace(old_css, new_css)
content = content.replace(old_css.replace('\n', '\r\n'), new_css.replace('\n', '\r\n'))

if content != original:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Slider fixed with pixel-based approach!")
    
    # Verify key changes
    checks = [
        ('slider.offsetWidth' in content, 'pixel-based translateX'),
        ('window.addEventListener("resize"' in content or 'window.addEventListener("resize"' in content, 'resize handler'),
        ('flex-shrink: 0' in content, 'slide flex-shrink'),
    ]
    for ok, label in checks:
        print(f"  {'OK' if ok else 'FAIL'}: {label}")
else:
    print("WARNING: No changes made!")
    # Debug: check what doesn't match
    for line in old_build_go.split('\n')[:5]:
        if line in original:
            print(f"  FOUND: {line.strip()[:60]}")
        else:
            crlf = line + '\r'
            if crlf in original:
                print(f"  FOUND(CRLF): {line.strip()[:60]}")
            else:
                print(f"  MISSING: {line.strip()[:60]}")

