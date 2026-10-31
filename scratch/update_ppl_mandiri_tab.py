import re

def update_ppl_mandiri():
    with open('ppl-mandiri.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS rules in <style>
    css_to_add = """
    /* ════ Video Analysis & Module Detail Styles (UAS Pembelajaran Pilihan) ════ */
    .detail-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }

    .detail-card {
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: var(--transition);
    }

    .detail-card:hover {
      background: var(--glass-hover);
      transform: translateY(-3px);
    }

    .detail-card-head {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--text-muted);
    }

    .detail-card-head .icon-circle {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--badge-bg);
      border: 1px solid var(--badge-border);
    }

    .detail-card-head svg {
      width: 16px;
      height: 16px;
      color: var(--primary-light);
    }

    .detail-card p {
      font-size: 0.88rem;
      line-height: 1.65;
      color: var(--text-secondary);
      margin: 0;
    }

    .detail-card.pro .icon-circle {
      background: rgba(34, 197, 94, 0.1);
      border-color: rgba(34, 197, 94, 0.2);
    }

    .detail-card.pro svg {
      color: #22c55e;
    }

    .detail-card.con .icon-circle {
      background: rgba(245, 158, 11, 0.1);
      border-color: rgba(245, 158, 11, 0.2);
    }

    .detail-card.con svg {
      color: #f59e0b;
    }

    .bottom-grid {
      display: grid;
      grid-template-columns: 350px 1fr;
      gap: 24px;
    }

    .theory-card {
      padding: 32px;
    }

    .theory-card h4 {
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .theory-card p {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 16px;
      line-height: 1.6;
    }

    .theory-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .theory-item {
      padding: 10px 14px;
      border-radius: 10px;
      background: var(--badge-bg);
      border: 1px solid var(--badge-border);
      font-size: 0.82rem;
      color: var(--text-primary);
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .theory-item::before {
      content: "✦";
      color: var(--primary-light);
      font-size: 0.7rem;
    }

    .video-showcase-card {
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .video-action-btns {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 6px;
    }

    .video-action-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
      cursor: pointer;
    }

    .video-action-btn.primary {
      background: #ef4444;
      color: #fff;
      border: 1px solid rgba(239, 68, 68, 0.4);
    }

    .video-action-btn.primary:hover {
      background: #dc2626;
      transform: translateY(-2px);
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.35);
    }

    .analysis-stage-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 20px;
    }

    .stage-card {
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      border: 1px solid var(--glass-border);
      min-width: 0;
      overflow: hidden;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }

    .stage-card-head {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--glass-border);
      min-width: 0;
    }

    .stage-tag {
      font-size: 0.68rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      padding: 4px 10px;
      border-radius: 50px;
    }

    .stage-tag.pendahuluan {
      background: rgba(59, 130, 246, 0.12);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.25);
    }

    .stage-tag.inti {
      background: rgba(168, 85, 247, 0.12);
      color: #c084fc;
      border: 1px solid rgba(168, 85, 247, 0.25);
    }

    .stage-tag.penutup {
      background: rgba(34, 197, 94, 0.12);
      color: #4ade80;
      border: 1px solid rgba(34, 197, 94, 0.25);
    }

    .stage-card h4 {
      font-size: 1.02rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0;
      display: flex;
      align-items: flex-start;
      gap: 8px;
      line-height: 1.4;
      flex: 1;
      min-width: 0;
      word-break: break-word;
      overflow-wrap: break-word;
    }

    .stage-card h4 svg {
      width: 18px;
      height: 18px;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .stage-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 12px;
      min-width: 0;
    }

    .stage-list > li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.84rem;
      line-height: 1.6;
      color: var(--text-secondary);
      min-width: 0;
    }

    .stage-list > li > svg {
      width: 15px;
      height: 15px;
      color: var(--primary-light);
      flex-shrink: 0;
      margin-top: 3px;
    }

    .stage-list > li > span {
      flex: 1;
      min-width: 0;
      word-break: break-word;
      overflow-wrap: break-word;
    }

    .stage-sublist {
      margin: 6px 0 0 16px;
      padding-left: 4px;
      list-style-type: disc;
    }

    .stage-sublist > li {
      display: list-item !important;
      font-size: 0.82rem;
      line-height: 1.55;
      color: var(--text-secondary);
      margin-bottom: 4px;
      min-width: 0;
      word-break: break-word;
      overflow-wrap: break-word;
    }

    .video-matrix-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }

    .matrix-card {
      padding: 26px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      border: 1px solid var(--glass-border);
    }

    .matrix-card.strength {
      border-left: 4px solid #22c55e;
    }

    .matrix-card.growth {
      border-left: 4px solid #f59e0b;
    }

    .matrix-card-head {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.95rem;
      font-weight: 700;
    }

    .matrix-card.strength .matrix-card-head {
      color: #22c55e;
    }

    .matrix-card.growth .matrix-card-head {
      color: #f59e0b;
    }

    .matrix-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .matrix-list li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.85rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }

    .matrix-card.strength .matrix-list li svg {
      color: #22c55e;
      flex-shrink: 0;
      margin-top: 3px;
      width: 15px;
      height: 15px;
    }

    .matrix-card.growth .matrix-list li svg {
      color: #f59e0b;
      flex-shrink: 0;
      margin-top: 3px;
      width: 15px;
      height: 15px;
    }

    @media (max-width: 1024px) {
      .analysis-stage-grid {
        grid-template-columns: 1fr;
      }
      .video-matrix-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>"""

    content = content.replace('  </style>', css_to_add)

    # 2. Add Tab Button in ct-tabs
    old_btn = """          <button class="ct-tab-btn" data-tab="tab-non-mengajar">
            <i data-lucide="clipboard-list"></i> Kegiatan Non Mengajar
          </button>"""

    new_btn = """          <button class="ct-tab-btn" data-tab="tab-non-mengajar">
            <i data-lucide="clipboard-list"></i> Kegiatan Non Mengajar
          </button>
          <button class="ct-tab-btn" data-tab="tab-pilihan">
            <i data-lucide="award"></i> Pembelajaran Pilihan (UAS PPL Mandiri)
          </button>"""

    if old_btn in content:
        content = content.replace(old_btn, new_btn)
        print("Tab button added!")
    else:
        print("Error: could not find tab button target")

    # 3. Add Tab Pane for tab-pilihan
    tab_pilihan_html = """
            <!-- ============================================== -->
            <!-- TAB 7: PEMBELAJARAN PILIHAN (UAS PPL MANDIRI) -->
            <!-- ============================================== -->
            <div class="ct-tab-pane" id="tab-pilihan">
              <div class="siklus-container">

                <!-- 1. Hero Card -->
                <div class="glass siklus-hero fade-in" id="sec-pilihan-hero">
                  <span class="sec-tag">UAS PPL Mandiri · Pembelajaran Pilihan</span>
                  <h2 class="siklus-title">
                    Pembelajaran Pilihan: Software Komputer (Sistem Operasi &amp; Perangkat Lunak Aplikasi)
                  </h2>
                  <div class="meta-row">
                    <div class="meta-item">
                      <i data-lucide="award"></i> Ujian Akhir Semester (UAS) PPL Mandiri
                    </div>
                    <div class="meta-item">
                      <i data-lucide="calendar"></i> 1 Pertemuan (2 × 40 menit / 80 menit)
                    </div>
                    <div class="meta-item">
                      <i data-lucide="building-2"></i> SMP Negeri 18 Malang
                    </div>
                    <div class="meta-item">
                      <i data-lucide="book-open"></i> Informatika Fase D (Kelas VII A)
                    </div>
                    <div class="meta-item">
                      <i data-lucide="layers"></i> Discovery Learning &amp; Kontekstual (CTL)
                    </div>
                    <div class="meta-item">
                      <i data-lucide="sticky-note"></i> Media: SIAP TEMPEL (Sticky Notes &amp; Papan Sekat)
                    </div>
                  </div>
                  <p class="hero-desc">
                    Praktik pembelajaran pilihan untuk Ujian Akhir Semester (UAS) PPL Mandiri di SMP Negeri 18 Malang pada materi Software Komputer. Pembelajaran mengintegrasikan pendekatan Kontekstual (CTL) dan model Discovery Learning melalui stimulus studi kasus kebutuhan Raka dalam memilih perangkat lunak, dipadukan metode partisipatif interaktif sticky notes pada sekat papan tulis untuk mengelompokkan ragam software sistem dan aplikasi secara kolaboratif.
                  </p>
                </div>

                <!-- 2. Detail Konteks & Sasaran Belajar -->
                <div class="detail-grid fade-in" id="sec-pilihan-detail">
                  <div class="glass detail-card">
                    <div class="detail-card-head">
                      <div class="icon-circle"><i data-lucide="map-pin"></i></div>
                      Konteks Pembelajaran
                    </div>
                    <p>
                      Studi kasus kontekstual kebutuhan Raka yang baru memperoleh komputer untuk tugas sekolah (mengetik, browsing, desain poster Canva, komunikasi via WhatsApp). Murid menganalisis hierarki perangkat lunak, membedakan peran OS dan aplikasi, serta memetakan fungsi software pada sekat papan tulis kelas.
                    </p>
                  </div>
                  <div class="glass detail-card">
                    <div class="detail-card-head">
                      <div class="icon-circle"><i data-lucide="target"></i></div>
                      Tujuan Pembelajaran
                    </div>
                    <ol style="padding-left: 18px; margin: 0; font-size: 0.88rem; line-height: 1.65; color: var(--text-secondary);">
                      <li style="margin-bottom: 6px;">Murid mampu menjelaskan pengertian software beserta contoh penggunaannya dalam kehidupan sehari-hari. (C1)</li>
                      <li>Murid mampu membedakan software sistem dan software aplikasi beserta contoh dan fungsinya. (C2)</li>
                    </ol>
                  </div>
                  <div class="glass detail-card pro">
                    <div class="detail-card-head">
                      <div class="icon-circle"><i data-lucide="check-circle-2"></i></div>
                      Kelebihan &amp; Dampak
                    </div>
                    <p>
                      Aktivitas partisipatif sticky notes di papan bersekat menciptakan iklim belajar yang kinetik dan kolaboratif (learning community), memfasilitasi visualisasi klasifikasi software secara komprehensif, serta melatih kecakapan murid memilih alat digital yang efisien.
                    </p>
                  </div>
                  <div class="glass detail-card con">
                    <div class="detail-card-head">
                      <div class="icon-circle"><i data-lucide="alert-triangle"></i></div>
                      Tantangan &amp; Evaluasi
                    </div>
                    <p>
                      Tantangan berupa misklasifikasi antara utilitas bawaan OS dengan aplikasi pihak ketiga diatasi dengan pertanyaan penuntun (scaffolding). Evaluasi formatif dinilai dari keaktifan diskusi, ketepatan kategori sticky notes, dan presentasi kelompok.
                    </p>
                  </div>
                </div>

                <!-- 3. Modul Ajar Software Komputer & Teori -->
                <div class="bottom-grid fade-in" id="sec-pilihan-modul">
                  <div class="glass theory-card">
                    <h4><i data-lucide="scroll-text"></i> Kajian Teori Pedagogik</h4>
                    <p>
                      Analisis perancangan modul ajar berbasis teori pembelajaran modern:
                    </p>
                    <div class="theory-list">
                      <div class="theory-item">Contextual Teaching &amp; Learning (CTL - Constructivism &amp; Inquiry)</div>
                      <div class="theory-item">Discovery Learning Model (Jerome Bruner - 6 Sintaks)</div>
                      <div class="theory-item">Collaborative Sticky-Note Mapping (Kinesthetic Learning)</div>
                      <div class="theory-item">Operating System &amp; Application Software Hierarchy</div>
                      <div class="theory-item">Capaian Pembelajaran Informatika Fase D (Sistem Komputer)</div>
                    </div>
                  </div>
                  <div class="files-container">
                    <div class="glass file-group">
                      <div class="file-group-head">
                        <span><i data-lucide="folder-open" style="width: 14px; height: 14px; vertical-align: middle; margin-right: 6px;"></i> Modul Ajar Pembelajaran Pilihan</span>
                      </div>
                      <div class="file-list">
                        <a href="files/dokumen/ppl2/rpp/siklus 4/Modul Ajar Pertemuan 13 - Software Komputer.pdf" class="file-row" target="_blank">
                          <span class="file-row-icon"><i data-lucide="file-text"></i></span>
                          <span class="file-row-info">
                            <strong>Modul Ajar Pertemuan 13 - Software Komputer.pdf</strong>
                            <span>PDF Dokumen Modul Ajar Informatika Fase D (UAS PPL Mandiri)</span>
                          </span>
                          <span class="file-row-tag">BUKA PDF</span>
                        </a>
                      </div>
                      <div style="margin-top: 14px; width: 100%; height: 480px; border-radius: var(--radius-sm); overflow: hidden; border: 1px solid var(--glass-border); background: var(--glass-bg);">
                        <iframe src="files/dokumen/ppl2/rpp/siklus 4/Modul Ajar Pertemuan 13 - Software Komputer.pdf" style="width: 100%; height: 100%; border: none;"></iframe>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 4. Video Player Showcase Card -->
                <div class="glass video-showcase-card fade-in" id="sec-pilihan-video">
                  <div style="position: relative; width: 100%; aspect-ratio: 16 / 9; border-radius: var(--radius-sm); overflow: hidden; border: 1px solid var(--glass-border); background: #000; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4);">
                    <iframe 
                      src="https://www.youtube-nocookie.com/embed/W_Dim2gjz1A?rel=0&amp;enablejsapi=1" 
                      title="Video Praktik Mengajar Siklus 4: Discovery Learning Software Komputer &amp; Media Sticky Notes" 
                      style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                      referrerpolicy="strict-origin-when-cross-origin" 
                      allowfullscreen>
                    </iframe>
                  </div>
                  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; padding: 4px 2px 2px;">
                    <div style="max-width: 68%;">
                      <span class="sec-tag" style="margin-bottom: 6px;">Rekaman Video Pembelajaran 24 Menit</span>
                      <h3 style="font-size: 1.12rem; font-weight: 800; color: var(--text-primary); margin: 0 0 4px;">Video Praktik Mengajar: Discovery Learning Software Komputer &amp; Media Sticky Notes</h3>
                      <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0; line-height: 1.5;">Rekaman pelaksanaan pembelajaran materi Software Komputer di SMP Negeri 18 Malang berbasis sintaks Discovery Learning, menampilkan studi kasus Raka, penugasan kelompok dengan sticky notes pada papan tulis bersekat, eksplorasi gawai, verifikasi presentasi kelompok, dan generalisasi konsep.</p>
                    </div>
                    <div class="video-action-btns" style="margin: 0;">
                      <a href="https://youtu.be/W_Dim2gjz1A" target="_blank" class="video-action-btn primary">
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" style="vertical-align: middle; margin-right: 4px;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg> Tonton di YouTube
                      </a>
                    </div>
                  </div>
                </div>

                <!-- 5. Detail Evaluasi 3 Tahap Pembelajaran Berdasarkan Rekaman Video -->
                <div class="analysis-stage-grid fade-in" id="sec-pilihan-tahapan">
                  <div class="glass stage-card">
                    <div class="stage-card-head">
                      <h4><i data-lucide="compass"></i> <span>Tahap Pendahuluan</span></h4>
                      <span class="stage-tag pendahuluan">Pendahuluan</span>
                    </div>
                    <ul class="stage-list">
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>Pembukaan &amp; Pengondisian Kelas:</strong> Guru memulai pembelajaran dengan memberikan salam, menyapa peserta didik, mengajak berdoa bersama, melakukan absensi, serta mengecek kesiapan belajar.</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>Apersepsi Kontekstual (Studi Kasus Raka):</strong> Guru memberikan stimulus berupa studi kasus tentang kebingungan Raka yang baru mendapatkan laptop dan <em>smartphone</em> namun belum tahu <em>software</em> apa saja yang tepat untuk mengetik tugas, mencari materi, berkomunikasi, dan membuat poster.</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>Pertanyaan Pemantik:</strong> Guru mengajukan pertanyaan kritis mengenai fungsi penting <em>software</em> (misalnya: apa yang terjadi jika laptop hardware-nya lengkap tapi tanpa <em>software</em>?, apa perbedaan Windows/Android dengan WhatsApp/Microsoft Word?).</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>Penyampaian Tujuan Pembelajaran:</strong> Guru menyampaikan tujuan agar peserta didik mampu menjelaskan pengertian <em>software</em>, membedakan jenis <em>software</em> (sistem dan aplikasi), serta mengidentifikasi contoh dan fungsinya.</span>
                      </li>
                    </ul>
                  </div>

                  <div class="glass stage-card">
                    <div class="stage-card-head">
                      <h4><i data-lucide="play-circle"></i> <span>Tahap Inti (Sintaks Discovery Learning)</span></h4>
                      <span class="stage-tag inti">Kegiatan Inti</span>
                    </div>
                    <ul class="stage-list">
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>1. Stimulation (Pemberian Stimulus):</strong> Guru mengarahkan peserta didik mengamati permasalahan Raka dan memberikan penjelasan awal mengenai konsep <em>software</em> sebagai kumpulan program atau instruksi yang bekerja bersama <em>hardware</em> dan <em>brainware</em>.</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>2. Problem Statement (Identifikasi Masalah):</strong> Peserta didik mengidentifikasi masalah terkait klasifikasi <em>software</em> sistem dan aplikasi, lalu merumuskan dugaan sementara yang akan dibuktikan melalui penugasan kelompok.</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>3. Data Collection (Pengumpulan Data):</strong>
                          <ul class="stage-sublist">
                            <li>Guru membagi peserta didik ke dalam kelompok beranggotakan 4–5 orang.</li>
                            <li>Setiap kelompok menempati satu sekat khusus pada papan tulis yang telah diberi pembatas/nomor kelompok.</li>
                            <li>Peserta didik mengunduh file PDF materi via WhatsApp Group kelas menggunakan <em>smartphone</em>.</li>
                            <li>Guru membagikan <strong>sticky note</strong> dan spidol kepada tiap kelompok untuk menuliskan nama <em>software</em>, jenis (<em>software</em> sistem atau aplikasi), dan fungsinya sebanyak-banyaknya.</li>
                          </ul>
                        </span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>4. Data Processing (Pengolahan Data):</strong> Peserta didik berdiskusi dalam kelompok, mengumpulkan contoh <em>software</em> dari materi dan pengalaman sehari-hari, menuliskannya secara spesifik pada <em>sticky note</em>, lalu mengelompokkannya pada sekat papan tulis kelompok masing-masing.</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>5. Verification (Pembuktian):</strong>
                          <ul class="stage-sublist">
                            <li>Perwakilan kelompok mempresentasikan hasil <em>sticky note</em> yang tertempel di sekat papan tulis, menjelaskan jumlah temuan, pengelompokan jenis <em>software</em>, serta solusi aplikasi untuk kasus Raka.</li>
                            <li>Kelompok lain memberikan tanggapan, dan guru memberikan umpan balik serta penguatan konsep.</li>
                          </ul>
                        </span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>6. Generalization (Menarik Kesimpulan):</strong> Guru bersama peserta didik menyimpulkan hubungan antara <em>hardware</em>, <em>software</em>, dan <em>brainware</em>, serta pentingnya memilih aplikasi yang tepat dalam pemecahan masalah sehari-hari.</span>
                      </li>
                    </ul>
                  </div>

                  <div class="glass stage-card">
                    <div class="stage-card-head">
                      <h4><i data-lucide="check-circle"></i> <span>Tahap Penutup</span></h4>
                      <span class="stage-tag penutup">Penutup</span>
                    </div>
                    <ul class="stage-list">
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>Rangkuman &amp; Refleksi:</strong> Guru bersama murid merangkum materi tentang pengertian, jenis, dan perbedaan <em>software</em> sistem serta aplikasi.</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>Refleksi Pembelajaran:</strong> Mengajak peserta didik merefleksikan bagaimana pemahaman tentang <em>software</em> membantu memilih aplikasi yang tepat dalam kehidupan sehari-hari.</span>
                      </li>
                      <li>
                        <i data-lucide="check-circle-2"></i>
                        <span><strong>Tindak Lanjut &amp; Doa:</strong> Guru menyampaikan informasi untuk pertemuan berikutnya dan menutup pembelajaran dengan doa bersama.</span>
                      </li>
                    </ul>
                  </div>
                </div>

                <!-- 6. Matriks Evaluasi & Refleksi Kritis Video -->
                <div class="video-matrix-grid fade-in" id="sec-pilihan-matriks">
                  <div class="glass matrix-card strength">
                    <div class="matrix-card-head">
                      <i data-lucide="thumbs-up"></i> Kelebihan &amp; Praktik Baik yang Teramati (Strengths)
                    </div>
                    <ul class="matrix-list">
                      <li>
                        <i data-lucide="check"></i>
                        <span><strong>Penggunaan Media Interaktif (<em>Sticky Notes</em> &amp; Papan Sekat):</strong> Pemanfaatan <em>sticky notes</em> pada papan tulis bersekat memberikan pengalaman belajar kinestetik yang sangat efektif membuat peserta didik aktif, antusias, dan berkolaborasi secara nyata dalam kelompok.</span>
                      </li>
                      <li>
                        <i data-lucide="check"></i>
                        <span><strong>Asesmen Visual Seketika (<em>Formative Assessment at a Glance</em>):</strong> Sekat papan tulis per kelompok memudahkan guru dan siswa melihat serta memeriksa ketepatan klasifikasi <em>software</em> (sistem vs aplikasi) secara visual dan transparan.</span>
                      </li>
                      <li>
                        <i data-lucide="check"></i>
                        <span><strong>Pembelajaran Kontekstual:</strong> Studi kasus Raka dan penggunaan contoh aplikasi harian (<em>WhatsApp, YouTube, Canva, Windows, Android</em>) membuat konsep teoretis menjadi sangat dekat dengan keseharian remaja.</span>
                      </li>
                    </ul>
                  </div>

                  <div class="glass matrix-card growth">
                    <div class="matrix-card-head">
                      <i data-lucide="trending-up"></i> Catatan Evaluasi Diri &amp; Rencana Tindak Lanjut (Growth Areas)
                    </div>
                    <ul class="matrix-list">
                      <li>
                        <i data-lucide="arrow-up-right"></i>
                        <span><strong>Manajemen Pergerakan Kelas:</strong> Perlu pengaturan giliran perwakilan kelompok saat menulis dan menempelkan <em>sticky notes</em> ke papan tulis agar mobilitas siswa lebih teratur dan tidak terjadi penumpukan di depan kelas.</span>
                      </li>
                      <li>
                        <i data-lucide="arrow-up-right"></i>
                        <span><strong>Variasi Warna <em>Sticky Notes</em>:</strong> Pada pelaksanaan berikutnya, dapat diterapkan pembagian warna <em>sticky notes</em> yang berbeda (misalnya satu warna khusus untuk <em>software</em> sistem dan warna lain untuk <em>software</em> aplikasi) guna meningkatkan kontras visual dan kecepatan analisis data di papan tulis.</span>
                      </li>
                    </ul>
                  </div>
                </div>

              </div>
            </div><!-- /tab-pilihan -->
"""

    old_pane_end = '            </div><!-- /tab-non-mengajar>'
    if old_pane_end in content:
        content = content.replace(old_pane_end, old_pane_end + '\n' + tab_pilihan_html)
        print("Tab pane added!")
    else:
        # Check without >
        old_pane_end_alt = '</div><!-- /tab-non-mengajar -->'
        if old_pane_end_alt in content:
            content = content.replace(old_pane_end_alt, old_pane_end_alt + '\n' + tab_pilihan_html)
            print("Tab pane added (alt)!")
        else:
            print("Error: could not find tab-non-mengajar end")

    # 4. Update tocData in <script>
    old_toc = """        'tab-non-mengajar': [
          { href: '#sec-hero-nm', icon: 'info', label: 'Ringkasan' },
          { href: '#sec-program-nm', icon: 'clipboard-list', label: 'Program Utama' },
          { href: '#sec-kompetensi-nm', icon: 'award', label: 'Kompetensi Guru' },
          { href: '#sec-dokumentasi-nm', icon: 'camera', label: 'Dokumentasi' }
        ]"""

    new_toc = """        'tab-non-mengajar': [
          { href: '#sec-hero-nm', icon: 'info', label: 'Ringkasan' },
          { href: '#sec-program-nm', icon: 'clipboard-list', label: 'Program Utama' },
          { href: '#sec-kompetensi-nm', icon: 'award', label: 'Kompetensi Guru' },
          { href: '#sec-dokumentasi-nm', icon: 'camera', label: 'Dokumentasi' }
        ],
        'tab-pilihan': [
          { href: '#sec-pilihan-hero', icon: 'award', label: 'Ringkasan UAS' },
          { href: '#sec-pilihan-detail', icon: 'layers', label: 'Konteks & Sasaran' },
          { href: '#sec-pilihan-modul', icon: 'book-open', label: 'Modul Software' },
          { href: '#sec-pilihan-video', icon: 'video', label: 'Video Pembelajaran' },
          { href: '#sec-pilihan-tahapan', icon: 'compass', label: 'Analisis 3 Tahap' },
          { href: '#sec-pilihan-matriks', icon: 'check-circle', label: 'Matriks Evaluasi' }
        ]"""

    if old_toc in content:
        content = content.replace(old_toc, new_toc)
        print("TOC data updated!")
    else:
        print("Error: could not find tocData target")

    with open('ppl-mandiri.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated ppl-mandiri.html")

update_ppl_mandiri()

