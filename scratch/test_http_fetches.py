import urllib.request
import urllib.parse
import json

with open('files/manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fotos = data['foto']
print(f"Total fotos to test: {len(fotos)}")

success = 0
failed = []

for f in fotos:
    src = f['src']
    # URL encode
    encoded_src = urllib.parse.quote(src, safe='/:')
    url = f"http://localhost/portofolio/{encoded_src}"
    
    # Try HEAD request
    req = urllib.request.Request(url, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            if resp.status == 200:
                success += 1
            else:
                failed.append((src, resp.status))
    except Exception as e:
        failed.append((src, str(e)))

print(f"Success: {success}, Failed: {len(failed)}")
if failed:
    for item in failed:
        print("  FAILED:", item)

