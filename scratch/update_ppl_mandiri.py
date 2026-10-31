with open('ppl-mandiri.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update div to video-action-btns
target_div = '''                    <div>
                      <a href="https://youtu.be/W_Dim2gjz1A" target="_blank" class="video-action-btn primary">'''
repl_div = '''                    <div class="video-action-btns">
                      <a href="https://youtu.be/W_Dim2gjz1A" target="_blank" class="video-action-btn primary">'''

if target_div in content:
    content = content.replace(target_div, repl_div)
    print("Replaced target_div successfully")
else:
    print("target_div not found!")

# 2. Add video-action-btn CSS into <style> if needed
style_needle = '''    .pilihan-video-text p {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin: 0;
    }'''

style_add = '''    .pilihan-video-text p {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin: 0;
    }

    /* Video Action Buttons */
    .video-action-btns {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .video-action-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 22px;
      border-radius: 50px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.2px;
      text-decoration: none !important;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      cursor: pointer;
      line-height: 1;
      white-space: nowrap;
    }

    .video-action-btn svg {
      width: 17px;
      height: 17px;
      flex-shrink: 0;
      transition: transform 0.25s ease;
    }

    .video-action-btn:hover svg {
      transform: scale(1.1);
    }

    .video-action-btn.primary {
      background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
      color: #ffffff !important;
      border: 1px solid rgba(255, 255, 255, 0.25) !important;
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.35) !important;
    }

    .video-action-btn.primary:hover {
      background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%) !important;
      color: #ffffff !important;
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(239, 68, 68, 0.5) !important;
    }

    .video-action-btn.primary:active {
      transform: translateY(0);
      box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3) !important;
    }'''

if style_needle in content:
    content = content.replace(style_needle, style_add)
    print("Replaced style_needle successfully")
else:
    print("style_needle not found!")

with open('ppl-mandiri.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished writing ppl-mandiri.html")

