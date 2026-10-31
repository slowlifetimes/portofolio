import json

with open('files/manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Replace the foto array with all photos from the website
data['foto'] = [
    # PPL Terbimbing (Siklus 1-3)
    {"src": "files/foto/siklus1/foto1.jpg", "caption": "Kegiatan Pembelajaran Siklus 1 (PPL Terbimbing)", "label": "PPL Terbimbing · Siklus 1"},
    {"src": "files/foto/siklus2/foto1.jpeg", "caption": "Kegiatan Pembelajaran Siklus 2 (PPL Terbimbing)", "label": "PPL Terbimbing · Siklus 2"},
    {"src": "files/foto/siklus3/foto1.jpeg", "caption": "Kegiatan Pembelajaran Siklus 3 (PPL Terbimbing)", "label": "PPL Terbimbing · Siklus 3"},

    # PPL Mandiri Siklus 1
    {"src": "files/foto/PPL Mandiri/Siklus 1/Pembukaan.jpeg", "caption": "Pembukaan Pembelajaran Siklus 1 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 1"},
    {"src": "files/foto/PPL Mandiri/Siklus 1/Kegiatan Inti Pembelajaran.jpeg", "caption": "Kegiatan Inti Pembelajaran Siklus 1 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 1"},
    {"src": "files/foto/PPL Mandiri/Siklus 1/Presentasi Kelompok.jpeg", "caption": "Presentasi Kelompok Siklus 1 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 1"},
    {"src": "files/foto/PPL Mandiri/Siklus 1/Presentasi Kelompok yang lain.jpeg", "caption": "Presentasi Kelompok Lain Siklus 1 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 1"},

    # PPL Mandiri Siklus 2
    {"src": "files/foto/PPL Mandiri/Siklus 2/Pendahuluan.png", "caption": "Pendahuluan Pembelajaran Siklus 2 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 2"},
    {"src": "files/foto/PPL Mandiri/Siklus 2/Kegiatan Inti Pembelajaran.png", "caption": "Kegiatan Inti Pembelajaran Siklus 2 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 2"},
    {"src": "files/foto/PPL Mandiri/Siklus 2/Presentasi Kelompok.png", "caption": "Presentasi Kelompok Siklus 2 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 2"},

    # PPL Mandiri Siklus 3
    {"src": "files/foto/PPL Mandiri/Siklus 3/Pendahuluan.png", "caption": "Pendahuluan Pembelajaran Siklus 3 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 3"},
    {"src": "files/foto/PPL Mandiri/Siklus 3/Kegiatan Praktik menggunakan Google Lens.png", "caption": "Praktik Menggunakan Google Lens Siklus 3 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 3"},
    {"src": "files/foto/PPL Mandiri/Siklus 3/Murid Menjawab LKPD.png", "caption": "Murid Menjawab LKPD Siklus 3 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 3"},

    # PPL Mandiri Siklus 4
    {"src": "files/foto/PPL Mandiri/Siklus 4/Diskusi Kelompok.jpg", "caption": "Diskusi Kelompok Siklus 4 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 4"},
    {"src": "files/foto/PPL Mandiri/Siklus 4/Hasil Pembelajaran Murid.jpg", "caption": "Hasil Pembelajaran Murid Siklus 4 (PPL Mandiri)", "label": "PPL Mandiri · Siklus 4"},

    # Siklus 4 extra photos (from siklus4 folder)
    {"src": "files/foto/siklus4/foto1.jpg", "caption": "Dokumentasi Pembelajaran Siklus 4 (1)", "label": "PPL Mandiri · Siklus 4"},
    {"src": "files/foto/siklus4/foto2.jpg", "caption": "Dokumentasi Pembelajaran Siklus 4 (2)", "label": "PPL Mandiri · Siklus 4"},
    {"src": "files/foto/siklus4/foto3.jpg", "caption": "Dokumentasi Pembelajaran Siklus 4 (3)", "label": "PPL Mandiri · Siklus 4"},
    {"src": "files/foto/siklus4/foto_3_Image22.jpg", "caption": "Dokumentasi Pembelajaran Siklus 4 (4)", "label": "PPL Mandiri · Siklus 4"},
    {"src": "files/foto/siklus4/foto_4_Image25.jpg", "caption": "Dokumentasi Pembelajaran Siklus 4 (5)", "label": "PPL Mandiri · Siklus 4"},
    {"src": "files/foto/siklus4/foto_5_Image28.jpg", "caption": "Dokumentasi Pembelajaran Siklus 4 (6)", "label": "PPL Mandiri · Siklus 4"},

    # Kegiatan Non Mengajar
    {"src": "files/foto/Kegiatan Non Mengajar/Bimbingan Lomba Coding.jpeg", "caption": "Bimbingan Lomba Coding", "label": "Kegiatan Non Mengajar"},
    {"src": "files/foto/Kegiatan Non Mengajar/Juara 2 Lomba Pictoblox Malang Young Coder Competition 2026 Kategori AI.jpeg", "caption": "Juara 2 Lomba Pictoblox Malang Young Coder 2026 Kategori AI", "label": "Kegiatan Non Mengajar"},
    {"src": "files/foto/Kegiatan Non Mengajar/Juara 3 Lomba Pictoblox Malang Young Coder Competition 2026 Kategori AI.jpeg", "caption": "Juara 3 Lomba Pictoblox Malang Young Coder 2026 Kategori AI", "label": "Kegiatan Non Mengajar"},
    {"src": "files/foto/Kegiatan Non Mengajar/Kegiatan Piket Sekolah.jpeg", "caption": "Kegiatan Piket Sekolah", "label": "Kegiatan Non Mengajar"},
    {"src": "files/foto/Kegiatan Non Mengajar/Keliling Mencatat Absensi.jpeg", "caption": "Keliling Mencatat Absensi Siswa", "label": "Kegiatan Non Mengajar"},
    {"src": "files/foto/Kegiatan Non Mengajar/Pembiasaan Budaya 5S.jpeg", "caption": "Pembiasaan Budaya 5S (Senyum, Sapa, Salam, Sopan, Santun)", "label": "Kegiatan Non Mengajar"},

    # Kegiatan Umum PPL
    {"src": "files/foto/kegiatan/Apel peringantan hari kartini.jpeg", "caption": "Apel Peringatan Hari Kartini", "label": "Kegiatan Sekolah"},
    {"src": "files/foto/kegiatan/penerimaan kegiatan PPL.jpeg", "caption": "Penerimaan Kegiatan PPL", "label": "Kegiatan PPL"},
    {"src": "files/foto/kegiatan/penjemputan kegiatan PPL.jpeg", "caption": "Penjemputan Kegiatan PPL", "label": "Kegiatan PPL"},
    {"src": "files/foto/kegiatan/Foto bersama guru pamong dan dosen pembimbing lapangan.jpeg", "caption": "Foto Bersama DPL dan Guru Pamong", "label": "Kegiatan PPL"},
    {"src": "files/foto/kegiatan/Diskusi Kelompok PPL untuk mengerjakan tugas di LMS.jpeg", "caption": "Diskusi Kelompok PPL di LMS", "label": "Kegiatan PPL"},
    {"src": "files/foto/kegiatan/Distribusi MBG.jpeg", "caption": "Distribusi Makan Bergizi Gratis (MBG)", "label": "Kegiatan Sekolah"},
    {"src": "files/foto/kegiatan/Pelaksanaan kegiatan workshop finalisasi artikel.jpeg", "caption": "Workshop Finalisasi Artikel", "label": "Kegiatan PPL"},
    {"src": "files/foto/kegiatan/Pelaksanaan kegiatan workshop proposal artikel.jpeg", "caption": "Workshop Proposal Artikel", "label": "Kegiatan PPL"},
    {"src": "files/foto/kegiatan/istighosah.jpeg", "caption": "Kegiatan Istighosah", "label": "Kegiatan Sekolah"},
]

with open('files/manifest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated foto array: {len(data['foto'])} photos total!")

