import re

def refine_tab_pilihan():
    with open('ppl-mandiri.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS for tab-pilihan
    # Find the old CSS block we added and replace it with polished, pristine styles
    old_css_start = content.find('/* ════ Video Analysis & Module Detail Styles (UAS Pembelajaran Pilihan) ════ */')
    if old_css_start == -1:
        print("Error: Could not find old css start")
        return

    old_css_end = content.find('</style>', old_css_start)
    if old_css_end == -1:
        print("Error: Could not find old css end")
        return

    new_css = """/* ════ Video Analysis & Module Detail Styles (UAS Pembelajaran Pilihan) ════ */
    .pilihan-container {
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    /* Hero Card */
    .pilihan-hero {
      padding: 36px 38px;
      position: relative;
      overflow: hidden;
      border-radius: var(--radius-sm);
      border: 1px solid var(--glass-border);
      background: linear-gradient(135deg, var(--glass-bg), rgba(99, 102, 241, 0.06));
    }
    .pilihan-hero h2 {
      font-size: 1.65rem;
      font-weight: 800;
      line-height: 1.3;
      margin: 10px 0 14px;
      letter-spacing: -0.01em;
      color: var(--text-primary);
    }
    .pilihan-meta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      margin-bottom: 20px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--glass-border);
    }
    .pilihan-meta-item {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.82rem;
      color: var(--text-secondary);
      background: var(--badge-bg);
      border: 1px solid var(--badge-border);
      padding: 4px 12px;
      border-radius: 100px;
      font-weight: 500;
    }
    .pilihan-meta-item svg {
      width: 14px;
      height: 14px;
      color: var(--primary-light);
    }
    .pilihan-hero-desc {
      font-size: 0.92rem;
      line-height: 1.75;
      color: var(--text-secondary);
      margin: 0;
    }

    /* Detail Grid (2x2 on desktop, 1 on mobile) */
    .pilihan-detail-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
    }
    @media (max-width: 768px) {
      .pilihan-detail-grid {
        grid-template-columns: 1fr;
      }
    }
    .pilihan-detail-card {
      padding: 22px 24px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: var(--transition);
    }
    .pilihan-detail-card:hover {
      transform: translateY(-2px);
      background: var(--glass-hover);
      border-color: rgba(99, 102, 241, 0.3);
    }
    .pilihan-detail-head {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }
    .pilihan-icon-circle {
      width: 34px;
      height: 34px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(99, 102, 241, 0.1);
      border: 1px solid rgba(99, 102, 241, 0.2);
      color: var(--primary-light);
      flex-shrink: 0;
    }
    .pilihan-icon-circle.pro {
      background: rgba(34, 197, 94, 0.1);
      border-color: rgba(34, 197, 94, 0.25);
      color: #22c55e;
    }
    .pilihan-icon-circle.con {
      background: rgba(245, 158, 11, 0.1);
      border-color: rgba(245, 158, 11, 0.25);
      color: #f59e0b;
    }
    .pilihan-icon-circle svg {
      width: 17px;
      height: 17px;
    }
    .pilihan-detail-card p {
      font-size: 0.88rem;
      line-height: 1.65;
      color: var(--text-secondary);
      margin: 0;
    }
    .pilihan-detail-card ol {
      margin: 0;
      padding-left: 20px;
      font-size: 0.88rem;
      line-height: 1.65;
      color: var(--text-secondary);
    }
    .pilihan-detail-card ol li {
      margin-bottom: 6px;
    }
    .pilihan-detail-card ol li:last-child {
      margin-bottom: 0;
    }

    /* Modul Section */
    .pilihan-modul-box {
      border-radius: var(--radius-sm);
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      overflow: hidden;
    }
    .pilihan-modul-head {
      padding: 20px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      background: rgba(99, 102, 241, 0.04);
      border-bottom: 1px solid var(--glass-border);
    }
    .pilihan-modul-head h3 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .pilihan-modul-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .pilihan-theory-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .pilihan-theory-chip {
      padding: 6px 14px;
      border-radius: 8px;
      background: var(--badge-bg);
      border: 1px solid var(--badge-border);
      font-size: 0.8rem;
      color: var(--text-secondary);
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .pilihan-theory-chip::before {
      content: "✦";
      color: var(--primary-light);
      font-size: 0.7rem;
    }
    .pilihan-pdf-frame {
      width: 100%;
      height: 520px;
      border-radius: var(--radius-sm);
      overflow: hidden;
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
    }

    /* Video Player Box */
    .pilihan-video-box {
      border-radius: var(--radius-sm);
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      overflow: hidden;
      box-shadow: var(--shadow);
    }
    .pilihan-video-player {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #000;
    }
    .pilihan-video-player iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }
    .pilihan-video-info {
      padding: 22px 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      background: rgba(99, 102, 241, 0.03);
      border-top: 1px solid var(--glass-border);
    }
    .pilihan-video-text {
      flex: 1;
      min-width: 280px;
    }
    .pilihan-video-text h3 {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--text-primary);
      margin: 0 0 6px;
    }
    .pilihan-video-text p {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin: 0;
    }

    /* Tahap Pembelajaran (Sequential Progression Cards) */
    .pilihan-stages-wrap {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .pilihan-stage-card {
      border-radius: var(--radius-sm);
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      overflow: hidden;
      transition: var(--transition);
    }
    .pilihan-stage-card:hover {
      border-color: rgba(99, 102, 241, 0.3);
      background: var(--glass-hover);
    }
    .pilihan-stage-header {
      padding: 18px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      border-bottom: 1px solid var(--glass-border);
    }
    .pilihan-stage-title-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .pilihan-stage-num {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .pilihan-stage-num.p1 {
      background: rgba(59, 130, 246, 0.15);
      color: #3b82f6;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }
    .pilihan-stage-num.p2 {
      background: rgba(168, 85, 247, 0.15);
      color: #a855f7;
      border: 1px solid rgba(168, 85, 247, 0.3);
    }
    .pilihan-stage-num.p3 {
      background: rgba(34, 197, 94, 0.15);
      color: #22c55e;
      border: 1px solid rgba(34, 197, 94, 0.3);
    }
    .pilihan-stage-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0;
    }
    .pilihan-stage-badge {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 4px 12px;
      border-radius: 100px;
    }
    .pilihan-stage-badge.p1 {
      background: rgba(59, 130, 246, 0.12);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.25);
    }
    .pilihan-stage-badge.p2 {
      background: rgba(168, 85, 247, 0.12);
      color: #c084fc;
      border: 1px solid rgba(168, 85, 247, 0.25);
    }
    .pilihan-stage-badge.p3 {
      background: rgba(34, 197, 94, 0.12);
      color: #4ade80;
      border: 1px solid rgba(34, 197, 94, 0.25);
    }
    .pilihan-stage-body {
      padding: 22px 24px;
    }

    /* Sintaks Grid inside Tahap Inti */
    .pilihan-sintaks-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }
    @media (max-width: 768px) {
      .pilihan-sintaks-grid {
        grid-template-columns: 1fr;
      }
    }
    .pilihan-sintaks-card {
      padding: 16px 18px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--glass-border);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .pilihan-sintaks-head {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--text-primary);
    }
    .pilihan-sintaks-tag {
      font-size: 0.68rem;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      background: rgba(168, 85, 247, 0.14);
      color: #c084fc;
      border: 1px solid rgba(168, 85, 247, 0.3);
    }
    .pilihan-sintaks-card p {
      font-size: 0.83rem;
      line-height: 1.6;
      color: var(--text-secondary);
      margin: 0;
    }
    .pilihan-sintaks-card ul {
      margin: 4px 0 0;
      padding-left: 18px;
      font-size: 0.82rem;
      line-height: 1.55;
      color: var(--text-secondary);
    }
    .pilihan-sintaks-card ul li {
      margin-bottom: 4px;
    }

    /* List items for Pendahuluan & Penutup */
    .pilihan-items-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .pilihan-items-list li {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 0.86rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }
    .pilihan-items-list li svg {
      width: 16px;
      height: 16px;
      color: var(--primary-light);
      flex-shrink: 0;
      margin-top: 3px;
    }

    /* Reflection Matrix (2 columns) */
    .pilihan-matrix-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
    }
    @media (max-width: 768px) {
      .pilihan-matrix-grid {
        grid-template-columns: 1fr;
      }
    }
    .pilihan-matrix-card {
      padding: 24px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .pilihan-matrix-card.strength {
      border-left: 4px solid #22c55e;
      background: linear-gradient(135deg, var(--glass-bg), rgba(34, 197, 94, 0.03));
    }
    .pilihan-matrix-card.growth {
      border-left: 4px solid #f59e0b;
      background: linear-gradient(135deg, var(--glass-bg), rgba(245, 158, 11, 0.03));
    }
    .pilihan-matrix-head {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.95rem;
      font-weight: 700;
    }
    .pilihan-matrix-card.strength .pilihan-matrix-head {
      color: #22c55e;
    }
    .pilihan-matrix-card.growth .pilihan-matrix-head {
      color: #f59e0b;
    }
    .pilihan-matrix-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .pilihan-matrix-list li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.85rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }
    .pilihan-matrix-card.strength .pilihan-matrix-list li svg {
      color: #22c55e;
      flex-shrink: 0;
      margin-top: 3px;
      width: 15px;
      height: 15px;
    }
    .pilihan-matrix-card.growth .pilihan-matrix-list li svg {
      color: #f59e0b;
      flex-shrink: 0;
      margin-top: 3px;
      width: 15px;
      height: 15px;
    }
"""

    content = content[:old_css_start] + new_css + content[old_css_end:]

    # 2. Update the HTML inside #tab-pilihan
    tab_start = content.find('<div class="ct-tab-pane" id="tab-pilihan">')
    if tab_start == -1:
        print("Error: Could not find tab-pilihan start")
        return

    tab_end = content.find('</div><!-- /tab-pilihan -->', tab_start)
    if tab_end == -1:
        print("Error: Could not find tab-pilihan end")
        return

    tab_end += len('</div><!-- /tab-pilihan -->')

    new_tab_html = """<div class="ct-tab-pane" id="tab-pilihan">
              <div class="pilihan-container">

                <!-- 1. Hero Card -->
                <div class="glass pilihan-hero fade-in" id="sec-pilihan-hero">
                  <span class="sec-tag">UAS PPL Mandiri · Pembelajaran Pilihan</span>
                  <h2>
                    Pembelajaran Pilihan: Software Komputer (Sistem Operasi &amp; Perangkat Lunak Aplikasi)
                  </h2>
                  <div class="pilihan-meta-row">
                    <span class="pilihan-meta-item">
                      <i data-lucide="award"></i> Ujian Akhir Semester (UAS) PPL Mandiri
                    </span>
                    <span class="pilihan-meta-item">
                      <i data-lucide="calendar"></i> 1 Pertemuan (2 × 40 menit / 80 menit)
                    </span>
                    <span class="pilihan-meta-item">
                      <i data-lucide="building-2"></i> SMP Negeri 18 Malang
                    </span>
                    <span class="pilihan-meta-item">
                      <i data-lucide="book-open"></i> Informatika Fase D (Kelas VII A)
                    </span>
                    <span class="pilihan-meta-item">
                      <i data-lucide="layers"></i> Discovery Learning &amp; Kontekstual (CTL)
                    </span>
                    <span class="pilihan-meta-item">
                      <i data-lucide="sticky-note"></i> Media: SIAP TEMPEL (Papan Bersekat)
                    </span>
                  </div>
                  <p class="pilihan-hero-desc">
                    Praktik pembelajaran pilihan untuk Ujian Akhir Semester (UAS) PPL Mandiri di SMP Negeri 18 Malang pada materi Software Komputer. Pembelajaran memadukan pendekatan Kontekstual (CTL) dan model Discovery Learning melalui stimulus studi kasus kebutuhan Raka dalam memilih perangkat lunak, dipadukan metode partisipatif interaktif <em>sticky notes</em> pada sekat papan tulis kelas untuk mengelompokkan ragam <em>software</em> sistem dan aplikasi secara kolaboratif.
                  </p>
                </div>

                <!-- 2. Detail Konteks & Sasaran Belajar (2x2 Grid) -->
                <div class="pilihan-detail-grid fade-in" id="sec-pilihan-detail">
                  <div class="pilihan-detail-card">
                    <div class="pilihan-detail-head">
                      <div class="pilihan-icon-circle"><i data-lucide="map-pin"></i></div>
                      <span>Konteks Pembelajaran</span>
                    </div>
                    <p>
                      Studi kasus kontekstual kebutuhan Raka yang baru memperoleh komputer untuk tugas sekolah (mengetik, browsing materi, desain poster Canva, komunikasi via WhatsApp). Murid menganalisis hierarki perangkat lunak, membedakan peran OS dan aplikasi, serta memetakan fungsi software pada sekat papan tulis kelas.
                    </p>
                  </div>

                  <div class="pilihan-detail-card">
                    <div class="pilihan-detail-head">
                      <div class="pilihan-icon-circle"><i data-lucide="target"></i></div>
                      <span>Tujuan Pembelajaran</span>
                    </div>
                    <ol>
                      <li><strong>Pemahaman Konseptual (C1):</strong> Murid mampu menjelaskan pengertian software beserta contoh penggunaannya dalam kehidupan sehari-hari secara tepat.</li>
                      <li><strong>Klasifikasi Fungsional (C2):</strong> Murid mampu membedakan software sistem dan software aplikasi beserta contoh dan fungsinya melalui diskusi kelompok.</li>
                    </ol>
                  </div>

                  <div class="pilihan-detail-card">
                    <div class="pilihan-detail-head">
                      <div class="pilihan-icon-circle pro"><i data-lucide="check-circle-2"></i></div>
                      <span>Kelebihan &amp; Dampak Positif</span>
                    </div>
                    <p>
                      Aktivitas partisipatif <em>sticky notes</em> di papan bersekat menciptakan iklim belajar yang kinetik dan kolaboratif (<em>learning community</em>), memfasilitasi visualisasi klasifikasi software secara komprehensif, serta melatih kecakapan murid memilih alat digital yang efisien dan bijak.
                    </p>
                  </div>

                  <div class="pilihan-detail-card">
                    <div class="pilihan-detail-head">
                      <div class="pilihan-icon-circle con"><i data-lucide="alert-triangle"></i></div>
                      <span>Tantangan &amp; Solusi Evaluasi</span>
                    </div>
                    <p>
                      Tantangan berupa misklasifikasi antara utilitas bawaan OS dengan aplikasi pihak ketiga diatasi dengan pertanyaan penuntun (<em>scaffolding</em>). Evaluasi formatif dinilai transparan dari keaktifan diskusi, ketepatan penempatan kategori <em>sticky notes</em>, dan presentasi kelompok.
                    </p>
                  </div>
                </div>

                <!-- 3. Modul Ajar Software Komputer & Kajian Teori -->
                <div class="pilihan-modul-box fade-in" id="sec-pilihan-modul">
                  <div class="pilihan-modul-head">
                    <h3>
                      <i data-lucide="folder-open" style="width: 20px; height: 20px; color: var(--primary-light);"></i>
                      Perangkat Pembelajaran Pilihan (Modul Ajar Pertemuan 13)
                    </h3>
                    <a href="files/dokumen/ppl2/rpp/siklus 4/Modul Ajar Pertemuan 13 - Software Komputer.pdf" class="file-row-tag" style="text-decoration:none; padding:6px 14px; font-size:0.78rem;" target="_blank">
                      <i data-lucide="external-link" style="width:13px; height:13px; margin-right:4px;"></i> Buka Tab Baru (PDF)
                    </a>
                  </div>
                  <div class="pilihan-modul-body">
                    <!-- Theory Chips -->
                    <div>
                      <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:var(--text-muted); display:block; margin-bottom:8px;">
                        Kajian Teori Pedagogik &amp; Landasan Kurikulum:
                      </span>
                      <div class="pilihan-theory-chips">
                        <span class="pilihan-theory-chip">Contextual Teaching &amp; Learning (CTL)</span>
                        <span class="pilihan-theory-chip">Discovery Learning Model (Jerome Bruner)</span>
                        <span class="pilihan-theory-chip">Kinesthetic Collaborative Sticky-Note Mapping</span>
                        <span class="pilihan-theory-chip">Software Hierarchy (OS, Application, Utility)</span>
                        <span class="pilihan-theory-chip">Capaian Pembelajaran Fase D Sistem Komputer</span>
                      </div>
                    </div>

                    <!-- PDF Viewer Frame -->
                    <div class="pilihan-pdf-frame">
                      <iframe src="files/dokumen/ppl2/rpp/siklus 4/Modul Ajar Pertemuan 13 - Software Komputer.pdf" style="width: 100%; height: 100%; border: none;"></iframe>
                    </div>
                  </div>
                </div>

                <!-- 4. Video Showcase Card -->
                <div class="pilihan-video-box fade-in" id="sec-pilihan-video">
                  <div class="pilihan-video-player">
                    <iframe 
                      src="https://www.youtube-nocookie.com/embed/W_Dim2gjz1A?rel=0&amp;enablejsapi=1" 
                      title="Video Praktik Mengajar Siklus 4: Discovery Learning Software Komputer &amp; Media Sticky Notes" 
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                      referrerpolicy="strict-origin-when-cross-origin" 
                      allowfullscreen>
                    </iframe>
                  </div>
                  <div class="pilihan-video-info">
                    <div class="pilihan-video-text">
                      <span class="sec-tag" style="margin-bottom: 6px;">Rekaman Video Praktik Mengajar 24 Menit</span>
                      <h3>Video Praktik Pembelajaran: Discovery Learning Software Komputer</h3>
                      <p>Rekaman pelaksanaan pembelajaran materi Software Komputer di SMP Negeri 18 Malang berbasis sintaks Discovery Learning, menampilkan studi kasus Raka, penugasan kelompok dengan sticky notes pada papan tulis bersekat, eksplorasi gawai, verifikasi presentasi kelompok, dan generalisasi konsep.</p>
                    </div>
                    <div>
                      <a href="https://youtu.be/W_Dim2gjz1A" target="_blank" class="video-action-btn primary">
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" style="vertical-align: middle; margin-right: 4px;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg> Tonton di YouTube
                      </a>
                    </div>
                  </div>
                </div>

                <!-- 5. Detail Evaluasi 3 Tahap Pembelajaran (Sequential Progression Cards) -->
                <div class="pilihan-stages-wrap fade-in" id="sec-pilihan-tahapan">
                  <!-- Tahap 1: Pendahuluan -->
                  <div class="pilihan-stage-card">
                    <div class="pilihan-stage-header">
                      <div class="pilihan-stage-title-wrap">
                        <span class="pilihan-stage-num p1">01</span>
                        <h4 class="pilihan-stage-title">Tahap Pendahuluan (Apersepsi &amp; Pengondisian Kelas)</h4>
                      </div>
                      <span class="pilihan-stage-badge p1">Pendahuluan · 10 Menit</span>
                    </div>
                    <div class="pilihan-stage-body">
                      <ul class="pilihan-items-list">
                        <li>
                          <i data-lucide="check-circle-2"></i>
                          <span><strong>Pembukaan &amp; Pengondisian Kelas:</strong> Guru memulai pembelajaran dengan memberikan salam, menyapa peserta didik, mengajak berdoa bersama, melakukan absensi, serta mengecek kesiapan fisik dan psikologis belajar.</span>
                        </li>
                        <li>
                          <i data-lucide="check-circle-2"></i>
                          <span><strong>Apersepsi Kontekstual (Studi Kasus Raka):</strong> Guru memberikan stimulus berupa studi kasus nyata mengenai kebingungan tokoh Raka yang baru memperoleh laptop dan smartphone tetapi belum mengetahui software apa saja yang cocok untuk mengetik tugas, mencari materi, berkomunikasi, dan mendesain poster.</span>
                        </li>
                        <li>
                          <i data-lucide="check-circle-2"></i>
                          <span><strong>Pertanyaan Pemantik Kritis:</strong> Guru memantik nalar kritis siswa melalui pertanyaan pemantik: <em>"Apa yang terjadi jika laptop hardware-nya sangat canggih namun tidak dipasang software sama sekali?"</em> dan <em>"Apa perbedaan mendasar antara sistem operasi (Windows/Android) dengan program aplikasi (WhatsApp/Word)?"</em></span>
                        </li>
                        <li>
                          <i data-lucide="check-circle-2"></i>
                          <span><strong>Penyampaian Tujuan &amp; Alur Belajar:</strong> Guru menguraikan tujuan pembelajaran agar siswa mampu memahami pengertian software, mengklasifikasikan jenis software sistem dan aplikasi, serta mengerti mekanisme kerja kolaboratif dengan media SIAP TEMPEL.</span>
                        </li>
                      </ul>
                    </div>
                  </div>

                  <!-- Tahap 2: Kegiatan Inti (6 Sintaks Discovery Learning) -->
                  <div class="pilihan-stage-card">
                    <div class="pilihan-stage-header">
                      <div class="pilihan-stage-title-wrap">
                        <span class="pilihan-stage-num p2">02</span>
                        <h4 class="pilihan-stage-title">Tahap Inti (Implementasi 6 Sintaks Discovery Learning &amp; Media SIAP TEMPEL)</h4>
                      </div>
                      <span class="pilihan-stage-badge p2">Kegiatan Inti · 60 Menit</span>
                    </div>
                    <div class="pilihan-stage-body">
                      <div class="pilihan-sintaks-grid">
                        <div class="pilihan-sintaks-card">
                          <div class="pilihan-sintaks-head">
                            <span class="pilihan-sintaks-tag">SINTAKS 1</span>
                            <span>Stimulation (Stimulus)</span>
                          </div>
                          <p>Guru mengarahkan siswa mencermati narasi kebutuhan software Raka dan menjelaskan kedudukan software sebagai jembatan interaksi antara hardware dan brainware (pengguna).</p>
                        </div>

                        <div class="pilihan-sintaks-card">
                          <div class="pilihan-sintaks-head">
                            <span class="pilihan-sintaks-tag">SINTAKS 2</span>
                            <span>Problem Statement</span>
                          </div>
                          <p>Siswa mengidentifikasi masalah utama: bagaimana mengelompokkan software yang beragam menjadi kategori sistem operasi dan aplikasi, lalu menyusun hipotesis kelompok.</p>
                        </div>

                        <div class="pilihan-sintaks-card">
                          <div class="pilihan-sintaks-head">
                            <span class="pilihan-sintaks-tag">SINTAKS 3</span>
                            <span>Data Collection</span>
                          </div>
                          <p>Siswa dibagi ke dalam kelompok (4–5 orang), menempati sekat khusus papan tulis, mengunduh PDF materi via WhatsApp Group kelas, serta menerima paket sticky notes dan spidol.</p>
                        </div>

                        <div class="pilihan-sintaks-card">
                          <div class="pilihan-sintaks-head">
                            <span class="pilihan-sintaks-tag">SINTAKS 4</span>
                            <span>Data Processing</span>
                          </div>
                          <p>Kelompok aktif berdiskusi mengeksplorasi gawai dan bahan ajar, menuliskan nama software dan fungsinya pada sticky notes, lalu menempelkannya ke kategori yang sesuai di sekat papan tulis.</p>
                        </div>

                        <div class="pilihan-sintaks-card">
                          <div class="pilihan-sintaks-head">
                            <span class="pilihan-sintaks-tag">SINTAKS 5</span>
                            <span>Verification (Pembuktian)</span>
                          </div>
                          <p>Perwakilan kelompok mempresentasikan hasil tempelan sticky note di papan tulis. Kelompok lain memverifikasi dan memberikan tanggapan, didampingi penguatan konsep dari guru.</p>
                        </div>

                        <div class="pilihan-sintaks-card">
                          <div class="pilihan-sintaks-head">
                            <span class="pilihan-sintaks-tag">SINTAKS 6</span>
                            <span>Generalization (Kesimpulan)</span>
                          </div>
                          <p>Guru bersama seluruh siswa menarik benang merah kesimpulan tentang klasifikasi hierarki software komputer dan solusi rekomendasi software yang paling efisien bagi kasus Raka.</p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Tahap 3: Penutup -->
                  <div class="pilihan-stage-card">
                    <div class="pilihan-stage-header">
                      <div class="pilihan-stage-title-wrap">
                        <span class="pilihan-stage-num p3">03</span>
                        <h4 class="pilihan-stage-title">Tahap Penutup (Refleksi &amp; Rencana Tindak Lanjut)</h4>
                      </div>
                      <span class="pilihan-stage-badge p3">Penutup · 10 Menit</span>
                    </div>
                    <div class="pilihan-stage-body">
                      <ul class="pilihan-items-list">
                        <li>
                          <i data-lucide="check-circle-2"></i>
                          <span><strong>Rangkuman Bersama:</strong> Guru membimbing siswa menyimpulkan kembali poin-poin utama materi: pengertian software, peran sistem operasi, serta ragam aplikasi penunjang produktivitas.</span>
                        </li>
                        <li>
                          <i data-lucide="check-circle-2"></i>
                          <span><strong>Refleksi Makna Pembelajaran:</strong> Siswa diajak merefleksikan bagaimana wawasan software membantu mereka memilih aplikasi yang aman, resmi, dan sesuai kebutuhan saat menggunakan smartphone maupun komputer sekolah.</span>
                        </li>
                        <li>
                          <i data-lucide="check-circle-2"></i>
                          <span><strong>Apresiasi &amp; Doa Penutup:</strong> Guru mengapresiasi keaktifan partisipasi setiap kelompok di sekat papan tulis, menyampaikan kisi-kisi pertemuan berikutnya, dan menutup pembelajaran dengan doa bersama.</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>

                <!-- 6. Matriks Evaluasi & Refleksi Kritis Video -->
                <div class="pilihan-matrix-grid fade-in" id="sec-pilihan-matriks">
                  <div class="pilihan-matrix-card strength">
                    <div class="pilihan-matrix-head">
                      <i data-lucide="thumbs-up"></i>
                      <span>Kelebihan &amp; Praktik Baik yang Teramati (Strengths)</span>
                    </div>
                    <ul class="pilihan-matrix-list">
                      <li>
                        <i data-lucide="check"></i>
                        <span><strong>Media Interaktif SIAP TEMPEL:</strong> Penggunaan papan bersekat dan <em>sticky notes</em> terbukti sangat efektif membangkitkan keaktifan kinestetik dan rasa kepemilikan kelompok (<em>sense of ownership</em>).</span>
                      </li>
                      <li>
                        <i data-lucide="check"></i>
                        <span><strong>Asesmen Formatif Visual Terbuka:</strong> Sekat bernomor di papan tulis memungkinkan guru memantau progres pemahaman seluruh kelompok secara visual dalam sekali pandang (*assessment at a glance*).</span>
                      </li>
                      <li>
                        <i data-lucide="check"></i>
                        <span><strong>Kontekstual &amp; Relevan:</strong> Mengaitkan konsep dengan studi kasus Raka dan aplikasi harian (WhatsApp, Canva, Word, Android) membuat teori komputer abstrak menjadi sangat aplikatif.</span>
                      </li>
                    </ul>
                  </div>

                  <div class="pilihan-matrix-card growth">
                    <div class="pilihan-matrix-head">
                      <i data-lucide="trending-up"></i>
                      <span>Catatan Evaluasi Diri &amp; Rencana Tindak Lanjut (Growth Areas)</span>
                    </div>
                    <ul class="pilihan-matrix-list">
                      <li>
                        <i data-lucide="arrow-up-right"></i>
                        <span><strong>Manajemen Mobilitas Kelas:</strong> Perlu pembagian giliran maju ke depan kelas yang lebih terjadwal agar pergerakan siswa menempelkan <em>sticky notes</em> berlangsung lebih tertib tanpa penumpukan.</span>
                      </li>
                      <li>
                        <i data-lucide="arrow-up-right"></i>
                        <span><strong>Variasi Kode Warna Sticky Notes:</strong> Pada siklus mendatang, dapat ditentukan warna spesifik (misal kuning untuk OS, hijau untuk aplikasi) guna memudahkan verifikasi visual dan analisis kategori di papan tulis.</span>
                      </li>
                    </ul>
                  </div>
                </div>

              </div>
            </div><!-- /tab-pilihan -->"""

    content = content[:tab_start] + new_tab_html + content[tab_end:]

    with open('ppl-mandiri.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully refined tab-pilihan in ppl-mandiri.html!")

refine_tab_pilihan()

