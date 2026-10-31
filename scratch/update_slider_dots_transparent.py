with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .slider-caption padding
old_cap_css = """      /* Caption overlay */
      .slider-caption {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px 24px 20px;
        background: linear-gradient(
          to top,
          rgba(10, 8, 40, 0.75) 0%,
          transparent 100%
        );
        display: flex;
        flex-direction: column;
        gap: 3px;
        pointer-events: none;
      }"""

new_cap_css = """      /* Caption overlay */
      .slider-caption {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 28px 24px 42px;
        background: linear-gradient(
          to top,
          rgba(10, 8, 40, 0.85) 0%,
          rgba(10, 8, 40, 0.4) 60%,
          transparent 100%
        );
        display: flex;
        flex-direction: column;
        gap: 3px;
        pointer-events: none;
        z-index: 5;
      }"""

if old_cap_css in content:
    content = content.replace(old_cap_css, new_cap_css)
    print("Replaced .slider-caption (LF)")
else:
    old_cap_css_crlf = old_cap_css.replace('\n', '\r\n')
    if old_cap_css_crlf in content:
        content = content.replace(old_cap_css_crlf, new_cap_css.replace('\n', '\r\n'))
        print("Replaced .slider-caption (CRLF)")
    else:
        print("old_cap_css not found!")

# 2. Update .slider-dots CSS
old_dots_css = """.slider-dots {
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

new_dots_css = """.slider-dots {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        align-items: center;
        gap: 6px;
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

      .slider-dots::-webkit-scrollbar {
        display: none;
      }

      .slider-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.45);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.6);
        border: none;
        cursor: pointer;
        transition: all 0.25s ease;
        padding: 0;
        flex-shrink: 0;
      }

      .slider-dot:hover {
        background: rgba(255, 255, 255, 0.85);
      }

      .slider-dot.active {
        background: #ffffff;
        box-shadow: 0 1px 5px rgba(0, 0, 0, 0.8);
        width: 18px;
        border-radius: 4px;
      }"""

if old_dots_css in content:
    content = content.replace(old_dots_css, new_dots_css)
    print("Replaced .slider-dots (LF)")
else:
    old_dots_css_crlf = old_dots_css.replace('\n', '\r\n')
    if old_dots_css_crlf in content:
        content = content.replace(old_dots_css_crlf, new_dots_css.replace('\n', '\r\n'))
        print("Replaced .slider-dots (CRLF)")
    else:
        print("old_dots_css not found!")

# 3. Update mobile media query
old_mq = """      @media (max-width: 600px) {
        .photo-slider {
          height: 260px;
        }
      }"""

new_mq = """      @media (max-width: 600px) {
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

if old_mq in content:
    content = content.replace(old_mq, new_mq)
    print("Replaced mobile media query (LF)")
else:
    old_mq_crlf = old_mq.replace('\n', '\r\n')
    if old_mq_crlf in content:
        content = content.replace(old_mq_crlf, new_mq.replace('\n', '\r\n'))
        print("Replaced mobile media query (CRLF)")
    else:
        print("old_mq not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")

