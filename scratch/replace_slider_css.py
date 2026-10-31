with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """      .photo-slider {
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

new_block = """      .photo-slider {
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

      /* Ambient blur background: fills aspect ratio gaps seamlessly */
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

if old_block in content:
    content = content.replace(old_block, new_block)
    print("Replaced CSS successfully (LF)!")
else:
    old_block_crlf = old_block.replace('\n', '\r\n')
    if old_block_crlf in content:
        content = content.replace(old_block_crlf, new_block.replace('\n', '\r\n'))
        print("Replaced CSS successfully (CRLF)!")
    else:
        print("CSS block not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

