import struct
import json

def get_image_size(path):
    try:
        with open(path, 'rb') as f:
            data = f.read(32)
            if data.startswith(b'\x89PNG\r\n\x1a\n'):
                w, h = struct.unpack('>LL', data[16:24])
                return w, h
        # For JPEG
        with open(path, 'rb') as f:
            data = f.read()
            i = 0
            while i < len(data) - 9:
                if data[i] == 0xFF:
                    marker = data[i+1]
                    if marker in [0xC0, 0xC1, 0xC2]:
                        h, w = struct.unpack('>HH', data[i+5:i+9])
                        return w, h
                    elif marker in [0xD8, 0xD9]:
                        i += 2
                    elif i + 4 <= len(data):
                        length = struct.unpack('>H', data[i+2:i+4])[0]
                        i += 2 + length
                    else:
                        break
                else:
                    i += 1
    except Exception as e:
        pass
    return None, None

with open('files/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

for p in manifest['foto']:
    w, h = get_image_size(p['src'])
    ratio = (w / h) if w and h else 0
    print(f"{w}x{h} (ratio={ratio:.2f}) -> {p['src']}")
