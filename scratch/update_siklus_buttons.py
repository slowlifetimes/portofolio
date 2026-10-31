import glob

siklus_files = glob.glob('ppl-mandiri-siklus*.html')
print("Files found:", siklus_files)

old_block = '''    .video-action-btn.primary {
      background: var(--primary);
      color: #fff;
      border: 1px solid var(--primary-light);
    }

    .video-action-btn.primary:hover {
      background: var(--primary-light);
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(99, 102, 241, 0.35);
    }'''

new_block = '''    .video-action-btn.primary {
      background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
      color: #ffffff !important;
      border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.35);
    }

    .video-action-btn.primary:hover {
      background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
      color: #ffffff !important;
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(239, 68, 68, 0.5);
    }'''

for path in siklus_files:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    if old_block in c:
        c = c.replace(old_block, new_block)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {path}")
    else:
        print(f"Old block not found directly in {path}")

