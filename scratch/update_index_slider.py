with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title if needed
old_h2 = '''                <h2
                  class="sec-title"
                  style="font-size: 1.5rem; margin-top: 4px; margin-bottom: 0"
                >
                  Dokumentasi Kegiatan PPL
                </h2>'''

new_h2 = '''                <h2
                  class="sec-title"
                  style="font-size: 1.5rem; margin-top: 4px; margin-bottom: 0"
                >
                  Momen Dokumentasi Praktik &amp; Kegiatan PPL
                </h2>'''

if old_h2 in content:
    content = content.replace(old_h2, new_h2)
    print("Updated h2")
else:
    # try with CRLF
    old_h2_crlf = old_h2.replace('\n', '\r\n')
    if old_h2_crlf in content:
        content = content.replace(old_h2_crlf, new_h2.replace('\n', '\r\n'))
        print("Updated h2 (CRLF)")
    else:
        print("old_h2 not matched, checking alternative...")
        alt_h2 = 'Dokumentasi Kegiatan PPL'
        if alt_h2 in content:
            content = content.replace(alt_h2, 'Momen Dokumentasi Praktik &amp; Kegiatan PPL')
            print("Replaced alt_h2 directly")

# 2. Update JS in index.html to encodeURI on src and add counter pill
old_build_go = '''        function build() {
          track.innerHTML = "";
          dotsWrap.innerHTML = "";

          // Dynamically scale track width based on slide count to prevent mobile flexbox bugs
          track.style.width = `${slides.length * 100}%`;

          slides.forEach((f, i) => {
            const slide = document.createElement("div");
            slide.className = "slider-slide";
            slide.style.width = `${100 / slides.length}%`;
            slide.innerHTML = `<img src="${f.src}" alt="${f.caption}" loading="lazy"/>`;
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
          const offset = -(current * (100 / slides.length));
          track.style.transform = `translateX(${offset}%)`;
          const f = slides[current];
          caption.innerHTML = `<span class="slider-cap-label">${f.label}</span><span class="slider-cap-text">${f.caption}</span>`;
          dotsWrap
            .querySelectorAll(".slider-dot")
            .forEach((d, i) => d.classList.toggle("active", i === current));
        }'''

new_build_go = '''        function build() {
          track.innerHTML = "";
          dotsWrap.innerHTML = "";

          // Dynamically scale track width based on slide count to prevent mobile flexbox bugs
          track.style.width = `${slides.length * 100}%`;

          slides.forEach((f, i) => {
            const slide = document.createElement("div");
            slide.className = "slider-slide";
            slide.style.width = `${100 / slides.length}%`;
            const encodedSrc = encodeURI(f.src);
            slide.innerHTML = `<img src="${encodedSrc}" alt="${f.caption}" loading="lazy"/>`;
            track.appendChild(slide);

            if (slides.length <= 20) {
              const dot = document.createElement("button");
              dot.className = "slider-dot";
              dot.setAttribute("aria-label", `Foto ${i + 1}`);
              dot.addEventListener("click", () => {
                go(i);
                resetAuto();
              });
              dotsWrap.appendChild(dot);
            }
          });
          prevBtn.style.display = nextBtn.style.display = "flex";
          dotsWrap.style.display = slides.length <= 20 ? "flex" : "none";
        }

        function go(idx) {
          current = (idx + slides.length) % slides.length;
          const offset = -(current * (100 / slides.length));
          track.style.transform = `translateX(${offset}%)`;
          const f = slides[current];
          caption.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:12px; width:100%;">
              <div style="min-width:0;">
                <span class="slider-cap-label">${f.label}</span>
                <span class="slider-cap-text">${f.caption}</span>
              </div>
              <span class="slider-cap-count">${current + 1} / ${slides.length}</span>
            </div>
          `;
          if (slides.length <= 20) {
            dotsWrap
              .querySelectorAll(".slider-dot")
              .forEach((d, i) => d.classList.toggle("active", i === current));
          }
        }'''

if old_build_go in content:
    content = content.replace(old_build_go, new_build_go)
    print("Updated build and go functions (LF)")
else:
    old_build_go_crlf = old_build_go.replace('\n', '\r\n')
    if old_build_go_crlf in content:
        content = content.replace(old_build_go_crlf, new_build_go.replace('\n', '\r\n'))
        print("Updated build and go functions (CRLF)")
    else:
        print("old_build_go not matched directly!")

# 3. Add styling for slider-cap-count if not present
if '.slider-cap-count' not in content:
    needle = '.slider-cap-text {'
    style_count = '''.slider-cap-count {
        font-size: 0.78rem;
        font-weight: 700;
        color: #ffffff;
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 5px 12px;
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.25);
        white-space: nowrap;
        letter-spacing: 0.5px;
        flex-shrink: 0;
      }

      .slider-cap-text {'''
    content = content.replace(needle, style_count)
    print("Added .slider-cap-count CSS")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished updating index.html")

