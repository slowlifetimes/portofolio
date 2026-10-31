with open('profil.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_p = '''            <p data-words>
              Melalui PPL ini, saya tidak sekadar belajar mengajar
              — saya belajar menjadi guru. Saya berlatih merancang
              pembelajaran Informatika yang interaktif, menyenangkan, serta ramah anak, serta terus berefleksi
              demi perbaikan berkelanjutan. Tujuan akhir saya adalah menjadi guru informatika
              profesional yang menginspirasi siswa menemukan keindahan logika teknologi dan berpikir komputasional.
            </p>'''

new_p = '''            <p data-words>
              Melalui Program PPG, saya tidak sekadar belajar mengajar saya belajar menjadi guru. Saya berlatih merancang pembelajaran Informatika yang interaktif, menyenangkan, serta ramah anak, dan terus berefleksi demi perbaikan berkelanjutan. Tujuan akhir saya adalah menjadi guru Informatika profesional yang mampu menginspirasi siswa untuk menemukan keindahan logika teknologi dan mengembangkan kemampuan berpikir komputasional.
            </p>'''

if old_p in content:
    content = content.replace(old_p, new_p)
    print("Replaced successfully!")
else:
    # Handle CRLF vs LF
    old_p_crlf = old_p.replace('\n', '\r\n')
    if old_p_crlf in content:
        content = content.replace(old_p_crlf, new_p.replace('\n', '\r\n'))
        print("Replaced with CRLF successfully!")
    else:
        print("Could not find old_p directly")

with open('profil.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished writing profil.html")

