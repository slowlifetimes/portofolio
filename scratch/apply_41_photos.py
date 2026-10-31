import json

with open('scratch/verify_all_41.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract photos list
start = text.find('photos = [')
end = text.find(']\n\nprint') + 1
photos_code = text[start + 9:end]
photos = eval(photos_code)

print(f"Loaded {len(photos)} photos.")

# 1. Update files/manifest.json
with open('files/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

manifest['foto'] = photos

with open('files/manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print("Updated files/manifest.json with 41 photos.")

# 2. Update js/data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

foto_idx = data_js.find('foto: [')
if foto_idx != -1:
    before = data_js[:foto_idx]
    formatted = "foto: [\n"
    for p in photos:
        formatted += f"    {{\n      src: {json.dumps(p['src'])},\n      caption: {json.dumps(p['caption'])},\n      label: {json.dumps(p['label'])},\n    }},\n"
    formatted += "  ],\n};\n"
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(before + formatted)
    print("Updated js/data.js with 41 photos.")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace script tags with versioned ones
idx_content = idx_content.replace('<script src="js/data.js"></script>', '<script src="js/data.js?v=20261031_03"></script>')
idx_content = idx_content.replace('<script src="js/main.js"></script>', '<script src="js/main.js?v=20261031_03"></script>')
idx_content = idx_content.replace('<script src="js/data.js?v=20261031_02"></script>', '<script src="js/data.js?v=20261031_03"></script>')
idx_content = idx_content.replace('<script src="js/main.js?v=20261031_02"></script>', '<script src="js/main.js?v=20261031_03"></script>')

# Format JS array for embedding directly in index.html
js_array_str = "        const ALL_WEBSITE_PHOTOS = " + json.dumps(photos, indent=10, ensure_ascii=False) + ";\n"

# Locate slider script in index.html
old_slider_start = '      /* ── Photo Slider ── */\n      (function () {'
old_slider_start_alt = '      /* ── Photo Slider ── */\r\n      (function () {'

# Find where slider IIFE starts
find_marker = '(function () {'
pos = idx_content.find(find_marker)
# Find the IIFE ending
end_marker = 'initSlider();\n      })();'
end_pos = idx_content.find(end_marker)
if end_pos == -1:
    end_marker = 'initSlider();\r\n      })();'
    end_pos = idx_content.find(end_marker)

print("Slider markers:", pos, end_pos)

new_slider_script = """(function () {
""" + js_array_str + """
        const track = document.getElementById("sliderTrack");
        const caption = document.getElementById("sliderCaption");
        const dotsWrap = document.getElementById("sliderDots");
        const prevBtn = document.getElementById("sliderPrev");
        const nextBtn = document.getElementById("sliderNext");
        const placeholder = document.getElementById("sliderPlaceholder");
        let slides = [],
          current = 0,
          timer = null;

        async function initSlider() {
          let data;
          try {
            data = await loadManifest();
          } catch (e) {
            data = null;
          }

          // Use ALL_WEBSITE_PHOTOS directly to guarantee all 41 photos load without browser caching issues
          let fotos = ALL_WEBSITE_PHOTOS;
          if (data && data.foto && data.foto.length >= ALL_WEBSITE_PHOTOS.length) {
            fotos = data.foto;
          }

          if (!fotos || !fotos.length) {
            showPlaceholder();
            return;
          }

          slides = fotos;
          build();
          go(0);
          startAuto();
        }

        function build() {
          track.innerHTML = "";
          dotsWrap.innerHTML = "";

          track.style.width = `${slides.length * 100}%`;

          slides.forEach((f, i) => {
            const slide = document.createElement("div");
            slide.className = "slider-slide";
            slide.style.width = `${100 / slides.length}%`;
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
          const offset = -(current * (100 / slides.length));
          track.style.transform = `translateX(${offset}%)`;
          const f = slides[current];
          caption.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:12px; width:100%;">
              <div style="min-width:0;">
                <span class="slider-cap-label">${f.label}</span>
                <span class="slider-cap-text">${f.caption}</span>
              </div>
              <span class="slider-cap-count">Foto ${current + 1} / ${slides.length}</span>
            </div>
          `;

          const dots = dotsWrap.querySelectorAll(".slider-dot");
          dots.forEach((d, i) => d.classList.toggle("active", i === current));
          if (dots[current]) {
            dots[current].scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
          }
        }

        function startAuto() {
          timer = setInterval(() => go(current + 1), 5000);
        }
        function resetAuto() {
          clearInterval(timer);
          startAuto();
        }

        function showPlaceholder() {
          placeholder.style.display = "flex";
          prevBtn.style.display = nextBtn.style.display = "none";
          dotsWrap.style.display = "none";
          if (window.lucide) lucide.createIcons({ nodes: [placeholder] });
        }

        prevBtn.addEventListener("click", () => {
          go(current - 1);
          resetAuto();
        });
        nextBtn.addEventListener("click", () => {
          go(current + 1);
          resetAuto();
        });

        // Swipe support
        let startX = 0;
        const slider = document.getElementById("photoSlider");
        slider.addEventListener(
          "touchstart",
          (e) => {
            startX = e.touches[0].clientX;
          },
          { passive: true },
        );
        slider.addEventListener(
          "touchend",
          (e) => {
            const dx = e.changedTouches[0].clientX - startX;
            if (Math.abs(dx) > 40) {
              go(current + (dx < 0 ? 1 : -1));
              resetAuto();
            }
          },
          { passive: true },
        );

        initSlider();
      })();"""

idx_content = idx_content[:pos] + new_slider_script + idx_content[end_pos + len(end_marker):]

# 4. Update slider-dots CSS in index.html
old_dots_css = """.slider-dots {
        position: absolute;
        bottom: 14px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 7px;
        z-index: 10;
      }

      .slider-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.4);
        border: none;
        cursor: pointer;
        transition: var(--transition);
        padding: 0;
      }

      .slider-dot.active {
        background: #fff;
        width: 22px;
        border-radius: 4px;
      }"""

new_dots_css = """.slider-dots {
        position: absolute;
        bottom: 12px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        align-items: center;
        gap: 5px;
        z-index: 10;
        max-width: 85%;
        overflow-x: auto;
        padding: 6px 12px;
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        scrollbar-width: none;
      }

      .slider-dots::-webkit-scrollbar {
        display: none;
      }

      .slider-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.4);
        border: none;
        cursor: pointer;
        transition: all 0.25s ease;
        padding: 0;
        flex-shrink: 0;
      }

      .slider-dot.active {
        background: var(--primary-light, #818cf8);
        width: 18px;
        border-radius: 4px;
      }"""

if old_dots_css in idx_content:
    idx_content = idx_content.replace(old_dots_css, new_dots_css)
    print("Replaced old_dots_css (LF)")
else:
    old_dots_css_crlf = old_dots_css.replace('\n', '\r\n')
    if old_dots_css_crlf in idx_content:
        idx_content = idx_content.replace(old_dots_css_crlf, new_dots_css.replace('\n', '\r\n'))
        print("Replaced old_dots_css (CRLF)")
    else:
        print("old_dots_css not found directly")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("Successfully written index.html!")

