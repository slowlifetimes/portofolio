import os
import glob
import re

def get_file_size_str(filepath):
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        if size >= 1024 * 1024:
            return f"{size / (1024 * 1024):.1f} MB"
        elif size >= 1024:
            return f"{size / 1024:.0f} KB"
        else:
            return f"{size} B"
    return "0 KB"

def build():
    # ── 1. Videos Data ──
    videos = [
        {
            "id": 1,
            "title": "Video Praktik Pembelajaran Mandiri Siklus 1",
            "subtitle": "Optimasi Penjadwalan & Berpikir Komputasional",
            "category": "PPL Mandiri · Siklus 1",
            "tag": "SIKLUS 1",
            "embed": "https://www.youtube.com/embed/7jQ2ASi6DLQ",
            "url": "https://youtu.be/7jQ2ASi6DLQ",
            "fase": "Fase D / Kelas VII A",
            "sekolah": "SMP Negeri 18 Malang",
            "desc": "Penerapan model Problem-Based Learning (PBL) pada materi berpikir komputasional optimasi penjadwalan. Menampilkan pembukaan kesepakatan smartphone, analogi visual wadah toples, aktivitas siswa di papan tulis, hingga evaluasi post-test barcode scan."
        },
        {
            "id": 2,
            "title": "Video Praktik Pembelajaran Mandiri Siklus 2",
            "subtitle": "Sistem Komputer & Struktur Data",
            "category": "PPL Mandiri · Siklus 2",
            "tag": "SIKLUS 2",
            "embed": "https://www.youtube.com/embed/uu7bIaCYDgw",
            "url": "https://youtu.be/uu7bIaCYDgw",
            "fase": "Fase D / Kelas VII",
            "sekolah": "SMP Negeri 18 Malang",
            "desc": "Pembelajaran interaktif materi struktur data dan sistem komputer dengan pendekatan kontekstual. Menampilkan tahap pendahuluan apersepsi, eksplorasi konsep terstruktur, serta presentasi hasil kerja kelompok siswa."
        },
        {
            "id": 3,
            "title": "Video Praktik Pembelajaran Mandiri Siklus 3",
            "subtitle": "Praktik Penyelidikan Hardware Komputer & Google Lens",
            "category": "PPL Mandiri · Siklus 3",
            "tag": "SIKLUS 3",
            "embed": "https://www.youtube.com/embed/Cg0jHbMSs0c",
            "url": "https://youtu.be/Cg0jHbMSs0c",
            "fase": "Fase D / Kelas VII F",
            "sekolah": "SMP Negeri 18 Malang",
            "desc": "Pembelajaran mendalam (deep learning) di laboratorium komputer melalui penyelidikan autentik membuka casing CPU, identifikasi komponen Motherboard, RAM, CPU, HDD dengan AI Google Lens, serta pengelompokan alur IPOS pada LKPD."
        },
        {
            "id": 4,
            "title": "Video Praktik Pembelajaran Mandiri Siklus 4",
            "subtitle": "Software Komputer & Media Interaktif SIAP TEMPEL",
            "category": "PPL Mandiri · Siklus 4",
            "tag": "SIKLUS 4",
            "embed": "https://www.youtube.com/embed/W_Dim2gjz1A",
            "url": "https://youtu.be/W_Dim2gjz1A",
            "fase": "Fase D / Kelas VII A",
            "sekolah": "SMP Negeri 18 Malang",
            "desc": "Penerapan model Discovery Learning materi perangkat lunak komputer berbantuan media konkret papan sekat dan sticky notes SIAP TEMPEL, berawal dari stimulus studi kasus nyata kebutuhan software Raka."
        }
    ]

    # ── 2. Photos Data ──
    photos = [
        # PPL Mandiri Siklus 1
        {
            "src": "files/foto/PPL Mandiri/Siklus 1/Pembukaan.jpeg",
            "title": "Tahap Pembukaan & Pengondisian Kelas",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 1",
            "desc": "Pendahuluan Pembelajaran · Doa Bersama, Presensi Kehadiran & Apersepsi Pembelajaran Siklus 1"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 1/Kegiatan Inti Pembelajaran.jpeg",
            "title": "Kegiatan Inti & Diskusi Terbimbing",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 1",
            "desc": "Kegiatan Inti · Peserta Didik Berdiskusi Menyelesaikan Studi Kasus Optimasi Penjadwalan"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 1/Presentasi Kelompok.jpeg",
            "title": "Presentasi Hasil Diskusi Kelompok",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 1",
            "desc": "Penyajian Hasil · Perwakilan Kelompok Memaparkan Solusi Algoritma di Depan Kelas"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 1/Presentasi Kelompok yang lain.jpeg",
            "title": "Tanggapan & Sesi Tanya Jawab Antar Kelompok",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 1",
            "desc": "Aktivitas Kelas · Kelompok Lain Menyimak, Memberikan Tanggapan & Guru Memberikan Penguatan"
        },
        # PPL Mandiri Siklus 2
        {
            "src": "files/foto/PPL Mandiri/Siklus 2/Pendahuluan.png",
            "title": "Tahap Pendahuluan & Apersepsi Pembelajaran",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 2",
            "desc": "Pendahuluan Pembelajaran · Doa Pembuka, Presensi Kehadiran, Motivasi & Penyampaian Tujuan Materi"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 2/Kegiatan Inti Pembelajaran.png",
            "title": "Kegiatan Inti & Eksplorasi Konsep Terbimbing",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 2",
            "desc": "Kegiatan Inti · Peserta Didik Berdiskusi dan Mengidentifikasi Konsep Sistem Komputer"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 2/Presentasi Kelompok.png",
            "title": "Presentasi Hasil Diskusi & Tanggapan Antar Kelompok",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 2",
            "desc": "Penyajian Hasil · Perwakilan Kelompok Mempresentasikan Solusi di Depan Kelas"
        },
        # PPL Mandiri Siklus 3
        {
            "src": "files/foto/PPL Mandiri/Siklus 3/Pendahuluan.png",
            "title": "Tahap Pendahuluan & Apersepsi Praktik Lab",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 3",
            "desc": "Pendahuluan Kelas, Presensi Kehadiran, Motivasi & Penjelasan Alur Pembelajaran Hardware"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 3/Kegiatan Praktik menggunakan Google Lens.png",
            "title": "Praktik Penyelidikan Hardware Berbantuan Google Lens",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 3",
            "desc": "Penyelidikan Langsung Komponen Internal CPU & Penelusuran Informasi Berbasis AI Google Lens"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 3/Murid Menjawab LKPD.png",
            "title": "Pengerjaan LKPD & Pengelompokan Komponen IPOS",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 3",
            "desc": "Diskusi Kelompok, Dokumentasi Komponen & Pengisian Lembar Kerja Peserta Didik (LKPD)"
        },
        # PPL Mandiri Siklus 4
        {
            "src": "files/foto/PPL Mandiri/Siklus 4/Screenshot 2026-10-31 144837.png",
            "title": "Tahap Pendahuluan & Stimulus Kasus Raka",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 4",
            "desc": "Pembukaan Kelas, Presensi Kehadiran, Apersepsi & Stimulus Studi Kasus Software Komputer"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 4/Diskusi Kelompok.jpg",
            "title": "Kegiatan Inti & Diskusi Kelompok SIAP TEMPEL",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 4",
            "desc": "Kolaborasi Antar Siswa Menyelesaikan Tantangan Pengelompokan Software dengan Papan Bersekat"
        },
        {
            "src": "files/foto/PPL Mandiri/Siklus 4/Hasil Pembelajaran Murid.jpg",
            "title": "Hasil Karya Pembelajaran Murid pada Media Papan Sekat",
            "category": "PPL Mandiri",
            "cat_code": "ppl-mandiri",
            "tag": "Siklus 4",
            "desc": "Dokumentasi Produk Pembelajaran Kelompok Menggunakan Sticky Notes dan Papan Bersekat SIAP TEMPEL"
        },
        # Kegiatan Non Mengajar
        {
            "src": "files/foto/Kegiatan Non Mengajar/Bimbingan Lomba Coding.jpeg",
            "title": "Bimbingan Siswa Lomba Coding & Pemrograman",
            "category": "Kegiatan Non Mengajar",
            "cat_code": "non-mengajar",
            "tag": "Prestasi Siswa",
            "desc": "Pendampingan persiapan dan pelatihan logika pemrograman bagi peserta didik sekolah"
        },
        {
            "src": "files/foto/Kegiatan Non Mengajar/Juara 2 Lomba Pictoblox Malang Young Coder Competition 2026 Kategori AI.jpeg",
            "title": "Juara 2 Malang Young Coder Competition 2026 (Kategori AI)",
            "category": "Kegiatan Non Mengajar",
            "cat_code": "non-mengajar",
            "tag": "Prestasi Siswa",
            "desc": "Prestasi membimbing peserta didik meraih Juara 2 pada ajang Malang Young Coder Competition"
        },
        {
            "src": "files/foto/Kegiatan Non Mengajar/Juara 3 Lomba Pictoblox Malang Young Coder Competition 2026 Kategori AI.jpeg",
            "title": "Juara 3 Malang Young Coder Competition 2026 (Kategori AI)",
            "category": "Kegiatan Non Mengajar",
            "cat_code": "non-mengajar",
            "tag": "Prestasi Siswa",
            "desc": "Prestasi membimbing peserta didik meraih Juara 3 pada ajang Malang Young Coder Competition"
        },
        {
            "src": "files/foto/Kegiatan Non Mengajar/Kegiatan Piket Sekolah.jpeg",
            "title": "Pelaksanaan Piket & Tata Tertib Sekolah",
            "category": "Kegiatan Non Mengajar",
            "cat_code": "non-mengajar",
            "tag": "Manajemen Sekolah",
            "desc": "Partisipasi aktif dalam piket sekolah harian, monitoring ketertiban dan presensi siswa"
        },
        {
            "src": "files/foto/Kegiatan Non Mengajar/Keliling Mencatat Absensi.jpeg",
            "title": "Monitoring Kehadiran Siswa di Kelas",
            "category": "Kegiatan Non Mengajar",
            "cat_code": "non-mengajar",
            "tag": "Manajemen Sekolah",
            "desc": "Kegiatan keliling kelas untuk merekap dan memverifikasi presensi kehadiran peserta didik"
        },
        {
            "src": "files/foto/Kegiatan Non Mengajar/Pembiasaan Budaya 5S.jpeg",
            "title": "Penyambutan Siswa & Pembiasaan Budaya 5S",
            "category": "Kegiatan Non Mengajar",
            "cat_code": "non-mengajar",
            "tag": "Budaya Positif",
            "desc": "Penerapan budaya Senyum, Sapa, Salam, Sopan, dan Santun di gerbang sekolah setiap pagi"
        },
        # PPL Terbimbing
        {
            "src": "files/foto/siklus1/foto1.jpg",
            "title": "Praktik PPL Terbimbing Siklus 1 (Insert Picture & Shapes)",
            "category": "PPL Terbimbing",
            "cat_code": "ppl-terbimbing",
            "tag": "Siklus 1",
            "desc": "Praktik pembelajaran Informatika kelas VII materi penyisipan objek dan teks dekoratif pada Ms. Word"
        },
        {
            "src": "files/foto/siklus2/foto1.jpeg",
            "title": "Praktik PPL Terbimbing Siklus 2 (Insert Table)",
            "category": "PPL Terbimbing",
            "cat_code": "ppl-terbimbing",
            "tag": "Siklus 2",
            "desc": "Praktik pembelajaran pemformatan tabel dan penataan data terstruktur pada Ms. Word"
        },
        {
            "src": "files/foto/siklus3/foto1.jpeg",
            "title": "Praktik PPL Terbimbing Siklus 3 (Symbol & Equation)",
            "category": "PPL Terbimbing",
            "cat_code": "ppl-terbimbing",
            "tag": "Siklus 3",
            "desc": "Praktik pembelajaran penyisipan formula matematika dan simbol ilmiah pada Ms. Word"
        },
        {
            "src": "files/foto/siklus4/foto1.jpg",
            "title": "Praktik PPL Terbimbing Siklus 4 (Evaluasi Akhir)",
            "category": "PPL Terbimbing",
            "cat_code": "ppl-terbimbing",
            "tag": "Siklus 4",
            "desc": "Pelaksanaan pembelajaran siklus 4 dan evaluasi pemahaman peserta didik di kelas"
        },
        {
            "src": "files/foto/siklus4/foto2.jpg",
            "title": "Media Pembelajaran Siklus 4 Terbimbing",
            "category": "PPL Terbimbing",
            "cat_code": "ppl-terbimbing",
            "tag": "Siklus 4",
            "desc": "Dokumentasi media dan bahan ajar yang digunakan pada PPL Terbimbing Siklus 4"
        },
        {
            "src": "files/foto/siklus4/foto3.jpg",
            "title": "Aktivitas Siswa Siklus 4 Terbimbing",
            "category": "PPL Terbimbing",
            "cat_code": "ppl-terbimbing",
            "tag": "Siklus 4",
            "desc": "Suasana kerja aktif dan kolaboratif peserta didik di ruang kelas PPL Terbimbing"
        },
        # Kegiatan Persekolahan PPL Terbimbing
        {
            "src": "files/foto/kegiatan/Apel peringantan hari kartini.jpeg",
            "title": "Apel Peringatan Hari Kartini",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Upacara Sekolah",
            "desc": "Pelaksanaan apel bersama bapak/ibu guru dan seluruh peserta didik dalam rangka Hari Kartini"
        },
        {
            "src": "files/foto/kegiatan/Foto bersama guru pamong dan dosen pembimbing lapangan.jpeg",
            "title": "Foto Bersama DPL dan Guru Pamong PPL",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Bimbingan PPL",
            "desc": "Dokumentasi koordinasi evaluasi dan refleksi bimbingan bersama DPL dan Guru Pamong"
        },
        {
            "src": "files/foto/kegiatan/penerimaan kegiatan PPL.jpeg",
            "title": "Penerimaan Mahasiswa PPL di Sekolah Mitra",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Orientasi PPL",
            "desc": "Penyambutan dan penerimaan resmi mahasiswa PPL PPG di SMP Negeri 18 Malang"
        },
        {
            "src": "files/foto/kegiatan/penjemputan kegiatan PPL.jpeg",
            "title": "Penjemputan & Pelepasan Mahasiswa PPL",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Pelepasan PPL",
            "desc": "Penjemputan resmi mahasiswa PPL PPG oleh pihak universitas setelah program selesai"
        },
        {
            "src": "files/foto/kegiatan/Diskusi Kelompok PPL untuk mengerjakan tugas di LMS.jpeg",
            "title": "Diskusi Kolaboratif PPL di LMS",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Refleksi LMS",
            "desc": "Kolaborasi mahasiswa PPL dalam menganalisis data observasi dan tugas perkuliahan LMS"
        },
        {
            "src": "files/foto/kegiatan/Distribusi MBG.jpeg",
            "title": "Distribusi Program Makan Bergizi Gratis (MBG)",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Sosial Sekolah",
            "desc": "Pendampingan distribusi program makanan bergizi gratis untuk mendukung nutrisi murid"
        },
        {
            "src": "files/foto/kegiatan/Pelaksanaan kegiatan workshop proposal artikel.jpeg",
            "title": "Workshop Penyusunan Proposal Artikel Ilmiah",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Workshop",
            "desc": "Kegiatan pembekalan penulisan artikel ilmiah berbasis hasil praktik PPL di sekolah mitra"
        },
        {
            "src": "files/foto/kegiatan/Pelaksanaan kegiatan workshop finalisasi artikel.jpeg",
            "title": "Workshop Finalisasi Artikel Ilmiah",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Workshop",
            "desc": "Review naskah dan penyempurnaan draft artikel ilmiah untuk publikasi hasil pembelajaran"
        },
        {
            "src": "files/foto/kegiatan/istighosah.jpeg",
            "title": "Kegiatan Istighosah & Doa Bersama Sekolah",
            "category": "Kegiatan Sekolah",
            "cat_code": "kegiatan-sekolah",
            "tag": "Religius Sekolah",
            "desc": "Kegiatan istighosah rutin guna memupuk karakter spiritual dan religius civitas sekolah"
        },
        # Foto Identitas & Refleksi
        {
            "src": "files/foto/profil.jpg",
            "title": "Foto Profil Calon Guru Profesional",
            "category": "Profil Guru",
            "cat_code": "kegiatan-sekolah",
            "tag": "Profil",
            "desc": "Foto portofolio profesional Muhammad Fajrul Fahmi, S.Kom - Mahasiswa PPG Prajabatan"
        },
        {
            "src": "files/foto/foto model guru.jpeg",
            "title": "Foto Model Guru Inspiratif",
            "category": "Profil Guru",
            "cat_code": "kegiatan-sekolah",
            "tag": "Model Guru",
            "desc": "Dokumentasi visual representasi figur guru inspiratif dan berpusat pada peserta didik"
        },
        {
            "src": "files/foto/foto refleksi.jpeg",
            "title": "Foto Refleksi Diri Praktik Mengajar",
            "category": "Profil Guru",
            "cat_code": "kegiatan-sekolah",
            "tag": "Refleksi Diri",
            "desc": "Dokumentasi kegiatan refleksi dan evaluasi praktik pembelajaran berkelanjutan"
        }
    ]

    # Verify each photo exists
    valid_photos = []
    for p in photos:
        if os.path.exists(p["src"]):
            p["size"] = get_file_size_str(p["src"])
            valid_photos.append(p)
        else:
            print("Warning: photo not found:", p["src"])
    print(f"Total valid photos: {len(valid_photos)}")

    # ── 3. Documents Categorization ──
    # Group all 173 documents into logical course categories
    doc_categories = {
        "PPL Mandiri (Semester 2)": {
            "code": "ppl-mandiri",
            "desc": "Modul Ajar Siklus 1 - 4 dan Lembar Kerja Pelaksanaan PPL Mandiri SMP Negeri 18 Malang",
            "files": []
        },
        "PPL Terbimbing (Semester 1)": {
            "code": "ppl-terbimbing",
            "desc": "RPP Siklus 1 - 3, Modul Praktikum, Penilaian Lampiran 7 & 8, serta Lembar Kerja PPL Terbimbing",
            "files": []
        },
        "Etika dan Profesionalisme Guru": {
            "code": "epg",
            "desc": "Lembar Kerja Topik 1-5, Dokumen Refleksi LK 2, dan Majalah UTS EPG",
            "files": []
        },
        "Projek Kepemimpinan": {
            "code": "projek-kepemimpinan",
            "desc": "Perencanaan Projek, Proposal Pengabdian UTS, PPT UAS, dan Dokumen Refleksi LK 2",
            "files": []
        },
        "Seminar Pendidikan Profesi Guru": {
            "code": "seminar-ppg",
            "desc": "Visi Pribadi Calon Guru (LK 1.2), Rancangan Inovatif SIAP TEMPEL (LK 4), dan Refleksi LK 2",
            "files": []
        },
        "Pembelajaran Sosial dan Emosional": {
            "code": "pse",
            "desc": "Lembar Kerja Topik 1-5 dan Refleksi Pengalaman Belajar LK 2",
            "files": []
        },
        "Pembelajaran Mendalam dan Asesmen Lanjut": {
            "code": "pm-lanjut",
            "desc": "Lembar Kerja Topik 1-5 dan Refleksi Pengalaman Belajar LK 2",
            "files": []
        },
        "Filosofi Pendidikan dan Pendidikan Nilai": {
            "code": "filosofi",
            "desc": "Tugas Alur MERDEKA Topik 1-4 dan Refleksi Pengalaman Belajar LK 2",
            "files": []
        },
        "Pemahaman tentang Peserta Didik dan Pembelajaran": {
            "code": "peserta-didik",
            "desc": "Tugas Alur MERDEKA Topik 1-4 tentang Karakteristik & Pemahaman Peserta Didik",
            "files": []
        },
        "Pembelajaran Mendalam dan Asesmen Dasar": {
            "code": "pm-dasar",
            "desc": "Prinsip Pengajaran dan Asesmen yang Efektif I (Topik 1-4 & Refleksi LK 2)",
            "files": []
        },
        "Pola Pikir Bertumbuh (Growth Mindset)": {
            "code": "growth-mindset",
            "desc": "Lembar Kerja LK 1.1 - LK 4.3 dan Refleksi Pengalaman Belajar LK 2",
            "files": []
        },
        "Computational Thinking": {
            "code": "computational-thinking",
            "desc": "Lembar Kerja Topik 1 - Topik 7 dan Refleksi Pengalaman Belajar LK 2",
            "files": []
        }
    }

    # Walk files/dokumen
    for root, dirs, files in os.walk('files/dokumen'):
        for f in sorted(files):
            rel = os.path.join(root, f).replace('\\', '/')
            ext = f.split('.')[-1].lower()
            if ext not in ['pdf', 'docx', 'doc', 'pptx']:
                continue
            
            size_str = get_file_size_str(rel)
            clean_name = os.path.splitext(f)[0]
            # Replace underscores for display
            display_name = clean_name.replace('_', ' ')

            # Map to category
            assigned_cat = None
            if "ppl2" in rel:
                assigned_cat = "PPL Mandiri (Semester 2)"
            elif "ppl1" in rel:
                assigned_cat = "PPL Terbimbing (Semester 1)"
            elif "Etika dan Profesionalisme Guru" in rel:
                assigned_cat = "Etika dan Profesionalisme Guru"
            elif "Projek Kepemimpinan" in rel:
                assigned_cat = "Projek Kepemimpinan"
            elif "Seminar Pendidikan Profesi Guru" in rel:
                assigned_cat = "Seminar Pendidikan Profesi Guru"
            elif "Pembelajaran Sosial" in rel:
                assigned_cat = "Pembelajaran Sosial dan Emosional"
            elif "Pembelajaran Mendalam dan Asesmen Lanjut" in rel:
                assigned_cat = "Pembelajaran Mendalam dan Asesmen Lanjut"
            elif "Pembelajaran Mendalam dan Asesmen" in rel or "Prinsip Pengajaran" in rel:
                assigned_cat = "Pembelajaran Mendalam dan Asesmen Dasar"
            elif "Filosofi Pendidikan dan Pendidikan Nilai" in rel:
                assigned_cat = "Filosofi Pendidikan dan Pendidikan Nilai"
            elif "Pemahaman tentang Peserta Didik dan Pembelajaran" in rel:
                assigned_cat = "Pemahaman tentang Peserta Didik dan Pembelajaran"
            elif "Pola Pikir Bertumbuh" in rel:
                assigned_cat = "Pola Pikir Bertumbuh (Growth Mindset)"
            elif "computationalThinking" in rel:
                assigned_cat = "Computational Thinking"

            if assigned_cat:
                doc_categories[assigned_cat]["files"].append({
                    "name": display_name,
                    "filename": rel,
                    "type": ext,
                    "size": size_str
                })
            else:
                print("Uncategorized document:", rel)

    total_docs = sum(len(c["files"]) for c in doc_categories.values())
    print(f"Total categorized documents: {total_docs}")

    # Return structured data for HTML rendering
    return videos, valid_photos, doc_categories, total_docs

if __name__ == "__main__":
    videos, photos, docs_cat, total_docs = build()
    print(f"Summary: {len(videos)} videos, {len(photos)} photos, {total_docs} documents.")
