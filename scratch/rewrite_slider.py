"""Completely rewrite the slider script and CSS in index.html."""

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

import re

# Find the entire script+style block: from <script> containing Photo Slider to </style>
# Pattern: from the IIFE script tag to the closing </style> before </body>
pattern = r'(<script>\s*/\*.*?Photo Slider.*?\*/.*?</script>\s*<style>.*?</style>)'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("ERROR: Could not find slider script+style block")
    # Try to find parts individually
    print("Script start:", "'/* ' Photo Slider" in content or "Photo Slider" in content)
    import sys
    sys.exit(1)

old_block = match.group(1)
print(f"Found block: {len(old_block)} chars, lines {content[:match.start()].count(chr(10))+1}-{content[:match.end()].count(chr(10))+1}")

new_block = r'''<script>
      /* ── Photo Slider (redesigned) ── */
      (function () {
        const ALL_WEBSITE_PHOTOS = ''' + re.search(r'const ALL_WEBSITE_PHOTOS = (\[.*?\]);', old_block, re.DOTALL).group(1) + r''';

        const el = {
          slider:      document.getElementById("photoSlider"),
          track:       document.getElementById("sliderTrack"),
          caption:     document.getElementById("sliderCaption"),
          dots:        document.getElementById("sliderDots"),
          prev:        document.getElementById("sliderPrev"),
          next:        document.getElementById("sliderNext"),
          placeholder: document.getElementById("sliderPlaceholder")
        };

        let photos = [], cur = 0, autoTimer = null;

        /* ── Init ── */
        async function init() {
          let data;
          try { data = await loadManifest(); } catch(e) { data = null; }
          let fotos = ALL_WEBSITE_PHOTOS;
          if (data && data.foto && data.foto.length >= ALL_WEBSITE_PHOTOS.length) {
            fotos = data.foto;
          }
          if (!fotos || !fotos.length) { showEmpty(); return; }
          photos = fotos;
          render();
          goTo(0);
          autoPlay();
        }

        /* ── Render slides & dots ── */
        function render() {
          el.track.innerHTML = "";
          el.dots.innerHTML  = "";

          photos.forEach(function(f, i) {
            // Slide
            var div = document.createElement("div");
            div.className = "ps-slide";
            var img = document.createElement("img");
            img.src = encodeURI(f.src);
            img.alt = f.caption;
            img.loading = "lazy";
            img.draggable = false;
            div.appendChild(img);
            el.track.appendChild(div);

            // Dot
            var dot = document.createElement("button");
            dot.className = "ps-dot";
            dot.setAttribute("aria-label", "Foto " + (i + 1));
            dot.addEventListener("click", function() { goTo(i); restartAuto(); });
            el.dots.appendChild(dot);
          });

          el.prev.style.display = el.next.style.display = "flex";
          el.dots.style.display = "flex";
        }

        /* ── Navigate to slide ── */
        function goTo(idx) {
          cur = ((idx % photos.length) + photos.length) % photos.length;
          el.track.style.transform = "translateX(-" + (cur * 100) + "%)";

          var f = photos[cur];
          el.caption.innerHTML =
            '<div class="ps-cap-inner">' +
              '<div style="min-width:0">' +
                '<span class="ps-cap-label">' + f.label + '</span>' +
                '<span class="ps-cap-text">' + f.caption + '</span>' +
              '</div>' +
              '<span class="ps-cap-count">Foto ' + (cur + 1) + ' / ' + photos.length + '</span>' +
            '</div>';

          var dots = el.dots.querySelectorAll(".ps-dot");
          for (var i = 0; i < dots.length; i++) {
            dots[i].classList.toggle("active", i === cur);
          }
          if (dots[cur]) {
            dots[cur].scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
          }
        }

        /* ── Auto-play ── */
        function autoPlay() { autoTimer = setInterval(function() { goTo(cur + 1); }, 5000); }
        function restartAuto() { clearInterval(autoTimer); autoPlay(); }

        /* ── Empty state ── */
        function showEmpty() {
          el.placeholder.style.display = "flex";
          el.prev.style.display = el.next.style.display = "none";
          el.dots.style.display = "none";
          if (window.lucide) lucide.createIcons({ nodes: [el.placeholder] });
        }

        /* ── Button events ── */
        el.prev.addEventListener("click", function() { goTo(cur - 1); restartAuto(); });
        el.next.addEventListener("click", function() { goTo(cur + 1); restartAuto(); });

        /* ── Touch/swipe ── */
        var touchX = 0;
        el.slider.addEventListener("touchstart", function(e) { touchX = e.touches[0].clientX; }, { passive: true });
        el.slider.addEventListener("touchend", function(e) {
          var dx = e.changedTouches[0].clientX - touchX;
          if (Math.abs(dx) > 40) { goTo(cur + (dx < 0 ? 1 : -1)); restartAuto(); }
        }, { passive: true });

        init();
      })();
    </script>
    <style>
      /* ── Photo Slider ── */
      .photo-slider {
        position: relative;
        overflow: hidden;
        border-radius: var(--radius);
        height: 420px;
        background: var(--glass-bg);
        touch-action: pan-y;
      }

      /* Track: flex row, each child = 100% width via CSS only */
      .slider-track {
        display: flex;
        height: 100%;
        transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1);
        will-change: transform;
      }

      /* Each slide: exactly 100% of the slider width */
      .ps-slide {
        width: 100%;
        min-width: 100%;
        height: 100%;
        position: relative;
        overflow: hidden;
      }
      .ps-slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        user-select: none;
        -webkit-user-drag: none;
      }

      /* Caption */
      .slider-caption {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        padding: 28px 24px 42px;
        background: linear-gradient(to top, rgba(10,8,40,0.85) 0%, rgba(10,8,40,0.4) 60%, transparent 100%);
        pointer-events: none;
        z-index: 5;
      }
      .ps-cap-inner {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        gap: 12px;
        width: 100%;
      }
      .ps-cap-label {
        display: block;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--primary-light);
        opacity: 0.9;
      }
      .ps-cap-text {
        display: block;
        font-size: 0.95rem;
        font-weight: 600;
        color: #fff;
      }
      .ps-cap-count {
        font-size: 0.78rem;
        font-weight: 700;
        color: #fff;
        background: rgba(15,23,42,0.65);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 5px 12px;
        border-radius: 50px;
        border: 1px solid rgba(255,255,255,0.25);
        white-space: nowrap;
        letter-spacing: 0.5px;
        flex-shrink: 0;
      }

      /* Prev / Next */
      .slider-btn {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 40px; height: 40px;
        border-radius: 50%;
        background: rgba(255,255,255,0.18);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.3);
        color: #fff;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer;
        transition: var(--transition);
        z-index: 10;
      }
      .slider-btn:hover {
        background: rgba(255,255,255,0.32);
        transform: translateY(-50%) scale(1.08);
      }
      .slider-btn-prev { left: 14px; }
      .slider-btn-next { right: 14px; }

      /* Dots */
      .slider-dots {
        position: absolute;
        bottom: 10px; left: 50%;
        transform: translateX(-50%);
        display: flex; align-items: center; gap: 6px;
        z-index: 10;
        max-width: 80%;
        overflow-x: auto;
        padding: 4px 0;
        background: transparent !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        border: none !important;
        border-radius: 0;
        box-shadow: none !important;
        scrollbar-width: none;
      }
      .slider-dots::-webkit-scrollbar { display: none; }
      .ps-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: rgba(255,255,255,0.45);
        box-shadow: 0 1px 3px rgba(0,0,0,0.6);
        border: none; cursor: pointer;
        transition: all 0.25s ease;
        padding: 0; flex-shrink: 0;
      }
      .ps-dot:hover { background: rgba(255,255,255,0.85); }
      .ps-dot.active {
        background: #fff;
        box-shadow: 0 1px 5px rgba(0,0,0,0.8);
        width: 18px; border-radius: 4px;
      }

      /* Placeholder */
      .slider-placeholder {
        position: absolute; inset: 0;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        gap: 14px; color: var(--text-muted);
        text-align: center; padding: 32px;
      }
      .slider-placeholder p { font-size: 0.85rem; line-height: 1.7; }
      .slider-placeholder code {
        background: var(--code-bg);
        padding: 2px 6px; border-radius: 4px;
        font-size: 0.8rem; color: var(--primary-light);
      }

      @media (max-width: 600px) {
        .photo-slider { height: 260px; }
        .slider-caption { padding: 20px 14px 34px; }
        .ps-cap-text { font-size: 0.82rem; line-height: 1.35; }
        .ps-cap-count { font-size: 0.72rem; padding: 4px 8px; }
        .slider-dots { bottom: 6px; max-width: 85%; }
      }
    </style>'''

content = content[:match.start()] + new_block + content[match.end():]

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Slider completely rewritten!")

# Verify no duplicate slider declarations
count = content.count('document.getElementById("photoSlider")')
print(f"  photoSlider references: {count} (should be 1)")

# Verify key CSS
print(f"  min-width: 100%: {'YES' if 'min-width: 100%' in content else 'NO'}")
print(f"  translateX percentage: {'YES' if 'cur * 100' in content else 'NO'}")
print(f"  ps-slide class: {'YES' if 'ps-slide' in content else 'NO'}")

