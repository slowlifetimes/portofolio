with open('js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_fn = '''async function fileExists(url) {
  if (window.location.protocol === "file:") return true; // Local file:// protocol compatibility
  try {
    const r = await fetch(url, { method: "HEAD" });
    if (r.ok) return true;
    const r2 = await fetch(url, { method: "GET" });
    return r2.ok;
  } catch {
    return false;
  }
}'''

new_fn = '''async function fileExists(url) {
  if (window.location.protocol === "file:") return true; // Local file:// protocol compatibility
  try {
    const encoded = encodeURI(url);
    const r = await fetch(encoded, { method: "HEAD" });
    if (r.ok) return true;
    const r2 = await fetch(encoded, { method: "GET" });
    return r2.ok;
  } catch {
    return false;
  }
}'''

if old_fn in content:
    content = content.replace(old_fn, new_fn)
    print("Replaced with LF")
else:
    old_fn_crlf = old_fn.replace('\n', '\r\n')
    if old_fn_crlf in content:
        content = content.replace(old_fn_crlf, new_fn.replace('\n', '\r\n'))
        print("Replaced with CRLF")
    else:
        print("Function not found!")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

