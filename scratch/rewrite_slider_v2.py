"""Rewrite slider with a clean approach: each slide is position:absolute, 
   only the visible one (and transition neighbor) are shown.
   Uses left: 0 and translateX on individual slides for animation."""

path = r"c:\laragon\www\portofolio\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

import re

# Find the script+style block
pattern = r'(<script>\s*/\*.*?Photo Slider.*?\*/.*?</script>\s*<style>.*?</style>)'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("ERROR: Could not find slider block")
    import sys; sys.exit(1)

# Extract the ALL_WEBSITE_PHOTOS array
photos_match = re.search(r'const ALL_WEBSITE_PHOTOS = (\[.*?\]);', match.group(1), re.DOTALL)
photos_array = photos_match.group(1)

new_block = '''<script>
      /* ── Photo Slider v2 ── */
      (function () {
        var ALL_WEBSITE_PHOTOS = ''' + photos_array + ''';

        var slider = document.getElementById("photoSlider");
        var track  = document.getElementById("sliderTrack");
        var caption = document.getElementById("sliderCaption");
        var dotsW  = document.getElementById("sliderDots");
        var btnP   = document.getElementById("sliderPrev");
        var btnN   = document.getElementById("sliderNext");
        var empty  = document.getElementById("sliderPlaceholder");

        var photos = [], cur = 0, auto = null;

        async function init() {
          var data;
          try { data = await loadManifest(); } catch(e) { data = null; }
          var f = ALL_WEBSITE_PHOTOS;
          if (data && data.foto && data.foto.length >= f.length) f = data.foto;
          if (!f || !f.length) { showEmpty(); return; }
          photos = f;
          build();
          goTo(0, true);
          play();
        }

        function build() {
          track.innerHTML = "";
          dotsW.innerHTML = "";
          for (var i = 0; i < photos.length; i++) {
            var s = document.createElement("div");
            s.className = "ps-slide";
            var img = document.createElement("img");
            img.src = encodeURI(photos[i].src);
            img.alt = photos[i].caption;
            img.loading = (i < 2) ? "eager" : "lazy";
            img.draggable = false;
            s.appendChild(img);
            track.appendChild(s);

            var d = document.createElement("button");
            d.className = "ps-dot";
            d.setAttribute("aria-label", "Foto " + (i+1));
            (function(idx){ d.addEventListener("click", function(){ goTo(idx); restart(); }); })(i);
            dotsW.appendChild(d);
          }
          btnP.style.display = btnN.style.display = "flex";
          dotsW.style.display = "flex";
        }

        function goTo(idx, instant) {
          cur = ((idx % photos.length) + photos.length) % photos.length;
          if (instant) track.style.transition = "none";
          track.style.transform = "translateX(-" + (cur * 100) + "%)";
          if (instant) {
            // Force reflow then restore transition
            track.offsetHeight;
            track.style.transition = "";
          }

          var f = photos[cur];
          caption.innerHTML =
            '<div class="ps-cap-row">' +
              '<div style="min-width:0">' +
                '<span class="ps-cap-label">' + f.label + '</span>' +
                '<span class="ps-cap-text">'  + f.caption + '</span>' +
              '</div>' +
              '<span class="ps-cap-count">Foto ' + (cur+1) + ' / ' + photos.length + '</span>' +
            '</div>';

          var dots = dotsW.querySelectorAll(".ps-dot");
          for (var i = 0; i < dots.length; i++) {
            if (i === cur) dots[i].classList.add("active");
            else dots[i].classList.remove("active");
          }
          if (dots[cur]) dots[cur].scrollIntoView({ behavior:"smooth", block:"nearest", inline:"center" });
        }

        function play()    { auto = setInterval(function(){ goTo(cur+1); }, 5000); }
        function restart()  { clearInterval(auto); play(); }

        function showEmpty() {
          empty.style.display = "flex";
          btnP.style.display = btnN.style.display = "none";
          dotsW.style.display = "none";
          if (window.lucide) lucide.createIcons({ nodes: [empty] });
        }

        btnP.addEventListener("click", function(){ goTo(cur-1); restart(); });
        btnN.addEventListener("click", function(){ goTo(cur+1); restart(); });

        var tx = 0;
        slider.addEventListener("touchstart", function(e){ tx = e.touches[0].clientX; }, {passive:true});
        slider.addEventListener("touchend", function(e){
          var dx = e.changedTouches[0].clientX - tx;
          if (Math.abs(dx) > 40) { goTo(cur + (dx<0?1:-1)); restart(); }
        }, {passive:true});

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

      /*
       * Track approach: display:flex with children width:100%.
       * translateX(-N00%) on the TRACK moves by N slides.
       * Key: track width = children count * 100% via flex,
       * and translateX% is relative to the track's own width.
       * So we set track width explicitly.
       */
      .slider-track {
        display: flex;
        height: 100%;
        transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1);
        will-change: transform;
      }

      .ps-slide {
        flex: 0 0 100%;   /* each slide = 100% of the PARENT (.photo-slider) */
        height: 100%;
        overflow: hidden;
        position: relative;
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
      .ps-cap-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        gap: 12px;
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

print("Slider v2 written!")
# Key: with flex: 0 0 100%, each slide is 100% of the flex container's PARENT width
# Because the flex container (.slider-track) doesn't have an explicit width,
# the 100% in flex-basis resolves against... hmm.
# 
# Actually, flex-basis: 100% resolves against the flex container's INNER main size.
# If the flex container has no explicit width, it's the available width from its parent.
# The parent is .photo-slider which has overflow:hidden and a defined width.
# So the flex container's available width = .photo-slider's content width.
# Each slide: flex: 0 0 100% = 100% of slider content width. CORRECT.
#
# translateX(-100%) on the TRACK:
# translateX percentage = relative to the element's own width.
# Track's own width = N * slider_width (because N children each 100% of slider width).
# So translateX(-100%) = N * slider_width pixels. WRONG for 1 slide.
#
# We need translateX(-(cur * 100 / N)%) to move cur slides.
# But that gives fractional values for non-round N.
#
# WAIT - I just realized: the track's computed width is NOT N * slider_width.
# With flex: 0 0 100%, the flex items won't shrink, so they overflow.
# But the flex container's width is determined by... it's complicated.
#
# Let me just test: if the track's width ends up = slider_width (because
# the track doesn't overflow its parent... no, overflow:hidden is on the parent,
# but the track itself has no overflow constraint).
#
# Actually, the track has display:flex. Its width = max(content width, parent width).
# Content width = sum of flex items = N * slider_width.
# Parent width = slider_width (from .photo-slider).
# So track width = N * slider_width.
# translateX(-100%) = -(N * slider_width). WRONG.
#
# I MUST use a different approach. Let me use translateX with FIXED PIXEL values.

print("\nWAIT - translateX percentage approach is WRONG for flex track!")
print("Need to use pixel-based approach instead.")
print("Rewriting go() to use pixel values...")

# Fix: change goTo to use pixel-based transform
content2 = content.replace(
    'track.style.transform = "translateX(-" + (cur * 100) + "%)";',
    'track.style.transform = "translateX(-" + (cur * slider.offsetWidth) + "px)";'
)
content2 = content2.replace(
    'track.style.transition = "none";\n          track.style.transform = "translateX(-" + (cur * 100) + "%)";',
    'track.style.transition = "none";\n          track.style.transform = "translateX(-" + (cur * slider.offsetWidth) + "px)";'
)

# Add resize handler before init()
content2 = content2.replace(
    '        init();\n      })();',
    '''        // Recalculate on resize
        window.addEventListener("resize", function() {
          if (photos.length) {
            track.style.transition = "none";
            track.style.transform = "translateX(-" + (cur * slider.offsetWidth) + "px)";
            track.offsetHeight; // force reflow
            track.style.transition = "";
          }
        });

        init();
      })();'''
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content2)

count = content2.count('slider.offsetWidth')
print(f"slider.offsetWidth occurrences: {count}")
print("Done! Pixel-based slider is ready.")

