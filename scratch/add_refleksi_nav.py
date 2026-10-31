"""Add 'Refleksi' nav item to all HTML pages, between the last dropdown and Berkas."""
import glob
import os

base = r"c:\laragon\www\portofolio"
html_files = glob.glob(os.path.join(base, "*.html"))

# The nav item to insert
refleksi_nav = '<li><a href="refleksi.html">Refleksi</a></li>'
refleksi_nav_active = '<li><a href="refleksi.html" class="active">Refleksi</a></li>'

# Pattern: we insert before the Berkas <li>
berkas_pattern = '<li><a href="berkas.html"'

count = 0
for fpath in html_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has refleksi nav
    if 'href="refleksi.html"' in content and fname != "refleksi.html":
        # Check if it already exists in nav
        # It might exist as a tab-btn link but not as a nav link
        # Let's check if it's in the nav-links section
        import re
        nav_match = re.search(r'<ul class="nav-links".*?</ul>', content, re.DOTALL)
        if nav_match and 'href="refleksi.html"' in nav_match.group(0):
            print(f"[{fname}] Already has Refleksi in navbar, skipping")
            continue

    # For refleksi.html itself, we already have the nav
    if fname == "refleksi.html":
        print(f"[{fname}] Skipping (already created with nav)")
        continue

    # Find the berkas li and insert before it
    idx = content.find(berkas_pattern)
    if idx == -1:
        print(f"[{fname}] WARNING: Could not find Berkas nav item")
        continue

    # Check what's before it (whitespace)
    # Find the start of the line
    line_start = content.rfind('\n', 0, idx) + 1
    indent = content[line_start:idx]

    nav_to_insert = refleksi_nav
    insert_text = f"{indent}{nav_to_insert}\n"

    content = content[:line_start] + insert_text + content[line_start:]

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    count += 1
    print(f"[{fname}] Added Refleksi nav item OK")

print(f"\nDone! Updated {count} files.")
