with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''          <!-- Nav Cards -->
          <div class="nav-cards fade-in" style="margin-top: 56px">
            <a href="profil.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="user-round"></i></div>
              <h3>Profil Mahasiswa</h3>
              <p>
                Kisah dari Gumul Kediri, inspirasi, dan tujuan menjadi guru
                profesional.
              </p>
            </a>
            <a href="artefak.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon">
                <i data-lucide="clipboard-list"></i>
              </div>
              <h3>Artefak Pembelajaran</h3>
              <p>
                RPP, media, dan hasil kerja siswa dari 3 siklus PPL Terbimbing.
              </p>
            </a>
            <a href="penilaian.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="bar-chart-2"></i></div>
              <h3>Penilaian GP & DPL</h3>
              <p>
                Lampiran 7 & 8 - instrumen penilaian dan catatan umpan balik per
                siklus.
              </p>
            </a>
            <a href="model-guru.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="star"></i></div>
              <h3>Model Guru Idaman</h3>
              <p>
                Misi, kompetensi, dan karakter guru profesional yang ingin
                diwujudkan.
              </p>
            </a>
            <a href="berkas.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="folder-open"></i></div>
              <h3>Berkas Proyek</h3>
              <p>
                Seluruh file dan dokumentasi PPL tersusun rapi dan siap diunduh.
              </p>
            </a>
          </div>'''

new_block = '''          <!-- Nav Cards -->
          <div class="nav-cards fade-in" style="margin-top: 56px">
            <a href="profil.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="user-round"></i></div>
              <h3>Profil Mahasiswa</h3>
              <p>
                Kisah dari Gumul Kediri, inspirasi, refleksi diri, dan tujuan menjadi guru profesional.
              </p>
            </a>
            <a href="model-guru.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="target"></i></div>
              <h3>Model Guru yang Dituju</h3>
              <p>
                Misi profesional dan 3 pilar visi: Berpikir Komputasional, TPACK, serta Literasi Digital.
              </p>
            </a>
            <a href="artefak.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="clipboard-list"></i></div>
              <h3>PPL Terbimbing</h3>
              <p>
                Modul ajar, media, dan hasil kerja siswa dari 3 siklus praktik terbimbing di SMPN 18 Malang.
              </p>
            </a>
            <a href="ppl-mandiri.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="laptop"></i></div>
              <h3>PPL Mandiri</h3>
              <p>
                Pelaksanaan 4 siklus mandiri, pembelajaran pilihan UAS software komputer, dan video praktik.
              </p>
            </a>
            <a href="filosofi-pendidikan.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="graduation-cap"></i></div>
              <h3>Mata Kuliah PPG</h3>
              <p>
                Dokumentasi tugas, refleksi, dan artefak perkuliahan Semester 1 &amp; Semester 2.
              </p>
            </a>
            <a href="berkas.html" class="nav-card glass glass-hover">
              <div class="nav-card-icon"><i data-lucide="folder-open"></i></div>
              <h3>Pusat Berkas &amp; Media</h3>
              <p>
                Koleksi lengkap modul ajar, media pembelajaran, galeri foto, rekaman video, dan dokumen.
              </p>
            </a>
          </div>'''

if old_block in content:
    content = content.replace(old_block, new_block)
    print("Replaced with LF!")
else:
    old_block_crlf = old_block.replace('\n', '\r\n')
    if old_block_crlf in content:
        content = content.replace(old_block_crlf, new_block.replace('\n', '\r\n'))
        print("Replaced with CRLF!")
    else:
        print("old_block not found directly!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished updating index.html")

