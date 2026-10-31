import os
import hashlib

folder = 'files/foto/siklus4'
files = os.listdir(folder)
for f in files:
    path = os.path.join(folder, f)
    size = os.path.getsize(path)
    with open(path, 'rb') as fp:
        md5 = hashlib.md5(fp.read()).hexdigest()
    print(f"{f}: {size} bytes, md5={md5}")

