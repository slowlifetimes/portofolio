with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update build() in index.html to insert .slider-bg-blur and .slider-main-img
old_slide_builder = """          slides.forEach((f, i) => {
            const slide = document.createElement("div");
            slide.className = "slider-slide";
            slide.style.width = `${100 / slides.length}%`;
            const encodedSrc = encodeURI(f.src);
            slide.innerHTML = `<img src="${encodedSrc}" alt="${f.caption}" loading="lazy"/>`;
            track.appendChild(slide);"""

new_slide_builder = """          slides.forEach((f, i) => {
            const slide = document.createElement("div");
            slide.className = "slider-slide";
            slide.style.width = `${100 / slides.length}%`;
            slide.style.flex = `0 0 ${100 / slides.length}%`;
            const encodedSrc = encodeURI(f.src);
            slide.innerHTML = `
              <div class="slider-bg-blur" style="background-image: url('${encodedSrc}');"></div>
              <img src="${encodedSrc}" alt="${f.caption}" class="slider-main-img" loading="lazy"/>
            `;
            track.appendChild(slide);"""

if old_slide_builder in content:
    content = content.replace(old_slide_builder, new_slide_builder)
    print("Replaced slide builder (LF)")
else:
    old_slide_builder_crlf = old_slide_builder.replace('\n', '\r\n')
    if old_slide_builder_crlf in content:
        content = content.replace(old_slide_builder_crlf, new_slide_builder.replace('\n', '\r\n'))
        print("Replaced slide builder (CRLF)")
    else:
        print("old_slide_builder not matched!")

# 2. Update CSS for photo-slider, slider-slide, slider-bg-blur, slider-main-img
old_css_part = """      /* ── Photo Slider Styles ── */
      .photo-slider {
        position: relative;
        overflow: hidden;
        border-radius: var(--radius);
        height: 420px;
        background: var(--glass-bg);
        touch-action: pan-y;
      }

      .slider-track {
        display: flex;
        height: 100%;
        transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1);
        will-change: transform;
      }

      .slider-slide {
        height: 100%;
        flex-shrink: 0;
        overflow: hidden;
      }

      .slider-slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transition: transform 0.6s ease;
      }

      .slider-slide img:hover {
        transform: scale(1.03);
      }"""

new_css_part = """      /* ── Photo Slider Styles ── */
      .photo-slider {
        position: relative;
        overflow: hidden;
        border-radius: var(--radius);
        height: 460px;
        background: #080b18;
        touch-action: pan-y;
      }

      .slider-track {
        display: flex;
        height: 100%;
        transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1);
        will-change: transform;
      }

      .slider-slide {
        position: relative;
        height: 100%;
        flex-shrink: 0;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      /* Ambient blur background to seamlessly fill aspect ratio gaps */
      .slider-bg-blur {
        position: absolute;
        inset: -20px;
        background-size: cover;
        background-position: center;
        filter: blur(30px) brightness(0.4);
        transform: scale(1.15);
        opacity: 0.8;
        z-index: 1;
        pointer-events: none;
      }

      /* Crisp main image: Fits completely (object-fit: contain) without cropping */
      .slider-main-img {
        position: relative;
        z-index: 2;
        max-width: 100%;
        max-height: 100%;
        width: auto;
        height: auto;
        object-fit: contain;
        display: block;
        margin: auto;
        border-radius: 4px;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.45);
        transition: transform 0.4s ease;
      }

      .slider-slide:hover .slider-main-img {
        transform: scale(1.02);
      }"""

if old_css_part in content:
    content = content.replace(old_css_part, new_css_part)
    print("Replaced CSS (LF)")
else:
    old_css_part_crlf = old_css_part.replace('\n', '\r\n')
    if old_css_part_crlf in content:
        content = content.replace(old_css_part_crlf, new_css_part.replace('\n', '\r\n'))
        print("Replaced CSS (CRLF)")
    else:
        print("old_css_part not matched directly!")

# 3. Update mobile query
old_mq = """      @media (max-width: 600px) {
        .photo-slider {
          height: 280px;
        }
        .slider-caption {
          padding: 20px 16px 36px;
        }
        .slider-cap-text {
          font-size: 0.85rem;
        }
        .slider-dots {
          bottom: 8px;
          max-width: 85%;
        }
      }"""

new_mq = """      @media (max-width: 600px) {
        .photo-slider {
          height: 300px;
        }
        .slider-caption {
          padding: 20px 14px 34px;
        }
        .slider-cap-text {
          font-size: 0.82rem;
          line-height: 1.35;
        }
        .slider-cap-count {
          font-size: 0.72rem;
          padding: 4px 8px;
        }
        .slider-dots {
          bottom: 6px;
          max-width: 85%;
        }
      }"""

if old_mq in content:
    content = content.replace(old_mq, new_mq)
    print("Replaced MQ (LF)")
else:
    old_mq_crlf = old_mq.replace('\n', '\r\n')
    if old_mq_crlf in content:
        content = content.replace(old_mq_crlf, new_mq.replace('\n', '\r\n'))
        print("Replaced MQ (CRLF)")
    else:
        print("old_mq not matched!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished updating index.html with perfect fit slider!")

