import hashlib

curated_photos = [
    # ── PPL Terbimbing ──
    {
        "src": "files/foto/siklus1/foto1.jpg",
        "caption": "Praktik PPL Terbimbing Siklus 1 (Insert Picture & Shapes)",
        "label": "PPL Terbimbing · Siklus 1"
    },
    {
        "src": "files/foto/siklus2/foto1.jpeg",
        "caption": "Praktik PPL Terbimbing Siklus 2 (Insert Table)",
        "label": "PPL Terbimbing · Siklus 2"
    },
    {
        "src": "files/foto/siklus3/foto1.jpeg",
        "caption": "Praktik PPL Terbimbing Siklus 3 (Symbol & Equation)",
        "label": "PPL Terbimbing · Siklus 3"
    },
    {
        "src": "files/foto/siklus4/foto1.jpg",
        "caption": "Praktik PPL Terbimbing Siklus 4 (Evaluasi Akhir)",
        "label": "PPL Terbimbing · Siklus 4"
    },
    {
        "src": "files/foto/siklus4/foto2.jpg",
        "caption": "Media Pembelajaran Siklus 4 Terbimbing",
        "label": "PPL Terbimbing · Siklus 4"
    },
    {
        "src": "files/foto/siklus4/foto3.jpg",
        "caption": "Aktivitas Siswa Siklus 4 Terbimbing",
        "label": "PPL Terbimbing · Siklus 4"
    },

    # ── PPL Mandiri Siklus 1 ──
    {
        "src": "files/foto/PPL Mandiri/Siklus 1/Pembukaan.jpeg",
        "caption": "Tahap Pembukaan & Pengondisian Kelas",
        "label": "PPL Mandiri · Siklus 1"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 1/Kegiatan Inti Pembelajaran.jpeg",
        "caption": "Kegiatan Inti & Diskusi Terbimbing",
        "label": "PPL Mandiri · Siklus 1"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 1/Presentasi Kelompok.jpeg",
        "caption": "Presentasi Hasil Diskusi Kelompok",
        "label": "PPL Mandiri · Siklus 1"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 1/Presentasi Kelompok yang lain.jpeg",
        "caption": "Tanggapan & Sesi Tanya Jawab Antar Kelompok",
        "label": "PPL Mandiri · Siklus 1"
    },

    # ── PPL Mandiri Siklus 2 ──
    {
        "src": "files/foto/PPL Mandiri/Siklus 2/Pendahuluan.png",
        "caption": "Tahap Pendahuluan & Apersepsi Pembelajaran",
        "label": "PPL Mandiri · Siklus 2"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 2/Kegiatan Inti Pembelajaran.png",
        "caption": "Kegiatan Inti & Eksplorasi Konsep Terbimbing",
        "label": "PPL Mandiri · Siklus 2"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 2/Presentasi Kelompok.png",
        "caption": "Presentasi Hasil Diskusi & Tanggapan Antar Kelompok",
        "label": "PPL Mandiri · Siklus 2"
    },

    # ── PPL Mandiri Siklus 3 ──
    {
        "src": "files/foto/PPL Mandiri/Siklus 3/Pendahuluan.png",
        "caption": "Tahap Pendahuluan & Apersepsi Praktik Lab",
        "label": "PPL Mandiri · Siklus 3"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 3/Kegiatan Praktik menggunakan Google Lens.png",
        "caption": "Praktik Penyelidikan Hardware Berbantuan Google Lens",
        "label": "PPL Mandiri · Siklus 3"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 3/Murid Menjawab LKPD.png",
        "caption": "Pengerjaan LKPD & Pengelompokan Komponen IPOS",
        "label": "PPL Mandiri · Siklus 3"
    },

    # ── PPL Mandiri Siklus 4 ──
    {
        "src": "files/foto/PPL Mandiri/Siklus 4/Screenshot 2026-10-31 144837.png",
        "caption": "Tahap Pendahuluan & Stimulus Kasus Raka",
        "label": "PPL Mandiri · Siklus 4"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 4/Diskusi Kelompok.jpg",
        "caption": "Kegiatan Inti & Diskusi Kelompok SIAP TEMPEL",
        "label": "PPL Mandiri · Siklus 4"
    },
    {
        "src": "files/foto/PPL Mandiri/Siklus 4/Hasil Pembelajaran Murid.jpg",
        "caption": "Hasil Karya Pembelajaran Murid pada Media Papan Sekat",
        "label": "PPL Mandiri · Siklus 4"
    },

    # ── Kegiatan Non Mengajar ──
    {
        "src": "files/foto/Kegiatan Non Mengajar/Bimbingan Lomba Coding.jpeg",
        "caption": "Bimbingan Siswa Lomba Coding & Pemrograman",
        "label": "Kegiatan Non Mengajar"
    },
    {
        "src": "files/foto/Kegiatan Non Mengajar/Juara 2 Lomba Pictoblox Malang Young Coder Competition 2026 Kategori AI.jpeg",
        "caption": "Juara 2 Malang Young Coder Competition 2026 (Kategori AI)",
        "label": "Kegiatan Non Mengajar"
    },
    {
        "src": "files/foto/Kegiatan Non Mengajar/Juara 3 Lomba Pictoblox Malang Young Coder Competition 2026 Kategori AI.jpeg",
        "caption": "Juara 3 Malang Young Coder Competition 2026 (Kategori AI)",
        "label": "Kegiatan Non Mengajar"
    },
    {
        "src": "files/foto/Kegiatan Non Mengajar/Kegiatan Piket Sekolah.jpeg",
        "caption": "Pelaksanaan Piket & Tata Tertib Sekolah",
        "label": "Kegiatan Non Mengajar"
    },
    {
        "src": "files/foto/Kegiatan Non Mengajar/Keliling Mencatat Absensi.jpeg",
        "caption": "Monitoring Kehadiran Siswa di Kelas",
        "label": "Kegiatan Non Mengajar"
    },
    {
        "src": "files/foto/Kegiatan Non Mengajar/Pembiasaan Budaya 5S.jpeg",
        "caption": "Penyambutan Siswa & Pembiasaan Budaya 5S",
        "label": "Kegiatan Non Mengajar"
    },

    # ── Kegiatan PPL & Sekolah ──
    {
        "src": "files/foto/kegiatan/Apel peringantan hari kartini.jpeg",
        "caption": "Apel Peringatan Hari Kartini",
        "label": "Kegiatan Sekolah"
    },
    {
        "src": "files/foto/kegiatan/Foto bersama guru pamong dan dosen pembimbing lapangan.jpeg",
        "caption": "Foto Bersama DPL dan Guru Pamong PPL",
        "label": "Kegiatan PPL"
    },
    {
        "src": "files/foto/kegiatan/penerimaan kegiatan PPL.jpeg",
        "caption": "Penerimaan Mahasiswa PPL di Sekolah Mitra",
        "label": "Kegiatan PPL"
    },
    {
        "src": "files/foto/kegiatan/penjemputan kegiatan PPL.jpeg",
        "caption": "Penjemputan & Pelepasan Mahasiswa PPL",
        "label": "Kegiatan PPL"
    },
    {
        "src": "files/foto/kegiatan/Diskusi Kelompok PPL untuk mengerjakan tugas di LMS.jpeg",
        "caption": "Diskusi Kolaboratif PPL di LMS",
        "label": "Kegiatan PPL"
    },
    {
        "src": "files/foto/kegiatan/Distribusi MBG.jpeg",
        "caption": "Distribusi Program Makan Bergizi Gratis (MBG)",
        "label": "Kegiatan Sekolah"
    },
    {
        "src": "files/foto/kegiatan/Pelaksanaan kegiatan workshop proposal artikel.jpeg",
        "caption": "Workshop Penyusunan Proposal Artikel Ilmiah",
        "label": "Kegiatan PPL"
    },
    {
        "src": "files/foto/kegiatan/Pelaksanaan kegiatan workshop finalisasi artikel.jpeg",
        "caption": "Workshop Finalisasi Artikel Ilmiah",
        "label": "Kegiatan PPL"
    },
    {
        "src": "files/foto/kegiatan/istighosah.jpeg",
        "caption": "Kegiatan Istighosah & Doa Bersama Sekolah",
        "label": "Kegiatan Sekolah"
    }
]

print(f"Curated list count: {len(curated_photos)}")

# Check duplicate paths
paths = [p['src'] for p in curated_photos]
if len(paths) != len(set(paths)):
    print("ERROR: Duplicate paths found!")
else:
    print("All 34 paths are unique!")

# Check duplicate hashes
hashes = {}
dup_hashes = []
for p in curated_photos:
    with open(p['src'], 'rb') as fp:
        h = hashlib.md5(fp.read()).hexdigest()
    if h in hashes:
        dup_hashes.append((p['src'], hashes[h]))
    else:
        hashes[h] = p['src']

if dup_hashes:
    print(f"ERROR: {len(dup_hashes)} duplicate hashes found:")
    for d, orig in dup_hashes:
        print(f"  {d} is identical to {orig}")
else:
    print("ALL 34 PHOTOS HAVE 100% UNIQUE CONTENT / HASHES!")

