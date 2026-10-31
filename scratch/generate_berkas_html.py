import os
import re
from build_berkas import build

videos, photos, doc_categories, total_docs = build()

# Generate HTML
html = f"""<!doctype html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>Pusat Berkas &amp; Multimedia | E-Portfolio PPL PPG Muhammad Fajrul Fahmi</title>
  <link rel="stylesheet" href="css/style.css" />
  <link rel="stylesheet" href="css/animate.css" />
  <style>
    /* ── Enhanced Berkas Page Styles ── */
    .berkas-stat-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }}
    .berkas-stat-card {{
      padding: 18px 20px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      gap: 16px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      box-shadow: var(--shadow);
      transition: transform 0.3s ease, border-color 0.3s ease;
    }}
    .berkas-stat-card:hover {{
      transform: translateY(-3px);
      border-color: rgba(99, 102, 241, 0.4);
    }}
    .berkas-stat-icon {{
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      font-size: 1.4rem;
    }}
    .stat-blue {{
      background: rgba(59, 130, 246, 0.15);
      color: #3b82f6;
    }}
    .stat-purple {{
      background: rgba(139, 92, 246, 0.15);
      color: #8b5cf6;
    }}
    .stat-red {{
      background: rgba(239, 68, 68, 0.15);
      color: #ef4444;
    }}
    .stat-emerald {{
      background: rgba(16, 185, 129, 0.15);
      color: #10b981;
    }}
    .berkas-stat-val {{
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--text-primary);
      line-height: 1.2;
    }}
    .berkas-stat-lbl {{
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    /* Search & Filter Bar */
    .berkas-search-box {{
      position: relative;
      margin-bottom: 24px;
    }}
    .berkas-search-input {{
      width: 100%;
      padding: 14px 18px 14px 46px;
      border-radius: 12px;
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      color: var(--text-primary);
      font-family: inherit;
      font-size: 0.92rem;
      backdrop-filter: blur(10px);
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }}
    .berkas-search-input:focus {{
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    }}
    .berkas-search-icon {{
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
      width: 18px;
      height: 18px;
    }}
    .berkas-clear-search {{
      position: absolute;
      right: 14px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      display: none;
      padding: 4px;
      border-radius: 50%;
    }}
    .berkas-clear-search:hover {{
      color: var(--text-primary);
    }}

    /* Sub-filter Pills */
    .filter-pills-wrap {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 22px;
    }}
    .filter-pill {{
      padding: 7px 16px;
      border-radius: 100px;
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      color: var(--text-secondary);
      font-size: 0.82rem;
      font-weight: 500;
      cursor: pointer;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .filter-pill:hover {{
      background: var(--glass-hover);
      color: var(--text-primary);
      border-color: rgba(99, 102, 241, 0.3);
    }}
    .filter-pill.active {{
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      color: #fff;
      border-color: transparent;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
    }}

    /* Video Cards Grid */
    .video-showcase-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 24px;
      margin-bottom: 30px;
    }}
    @media (max-width: 640px) {{
      .video-showcase-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .video-card-glass {{
      border-radius: 14px;
      overflow: hidden;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .video-card-glass:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
      border-color: rgba(99, 102, 241, 0.35);
    }}
    .video-player-wrap {{
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #000;
    }}
    .video-player-wrap iframe {{
      width: 100%;
      height: 100%;
      border: none;
    }}
    .video-card-body {{
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      flex: 1;
    }}
    .video-card-tag {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 10px;
      border-radius: 100px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      background: rgba(239, 68, 68, 0.12);
      color: #ef4444;
      border: 1px solid rgba(239, 68, 68, 0.25);
      align-self: flex-start;
    }}
    .video-card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0;
      line-height: 1.35;
    }}
    .video-card-subtitle {{
      font-size: 0.84rem;
      color: var(--primary-light);
      font-weight: 600;
    }}
    .video-card-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 0.78rem;
      color: var(--text-muted);
      border-top: 1px dashed var(--glass-border);
      border-bottom: 1px dashed var(--glass-border);
      padding: 8px 0;
    }}
    .video-card-meta span {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .video-card-desc {{
      font-size: 0.84rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin: 0;
      flex: 1;
    }}
    .video-card-footer {{
      margin-top: 6px;
      padding-top: 10px;
    }}

    /* Photo Cards Grid */
    .photo-gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 18px;
      margin-bottom: 30px;
    }}
    .photo-card-glass {{
      border-radius: 12px;
      overflow: hidden;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      cursor: pointer;
    }}
    .photo-card-glass:hover {{
      transform: translateY(-4px);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
      border-color: rgba(99, 102, 241, 0.4);
    }}
    .photo-card-thumb {{
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 10;
      overflow: hidden;
      background: rgba(15, 23, 42, 0.06);
    }}
    .photo-card-thumb img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.45s ease;
    }}
    .photo-card-glass:hover .photo-card-thumb img {{
      transform: scale(1.08);
    }}
    .photo-zoom-overlay {{
      position: absolute;
      top: 10px;
      right: 10px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(4px);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transform: scale(0.85);
      transition: all 0.25s ease;
    }}
    .photo-card-glass:hover .photo-zoom-overlay {{
      opacity: 1;
      transform: scale(1);
    }}
    .photo-card-body {{
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      flex: 1;
    }}
    .photo-card-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}
    .photo-tag {{
      padding: 2px 8px;
      border-radius: 100px;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      background: rgba(99, 102, 241, 0.12);
      color: var(--primary-light);
      border: 1px solid rgba(99, 102, 241, 0.2);
    }}
    .photo-size {{
      font-size: 0.72rem;
      color: var(--text-muted);
    }}
    .photo-card-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0;
      line-height: 1.35;
    }}
    .photo-card-desc {{
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.45;
      margin: 0;
      flex: 1;
    }}
    .photo-card-action {{
      margin-top: 6px;
      display: flex;
      justify-content: flex-end;
    }}
    .photo-open-link {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--primary-light);
      text-decoration: none;
      padding: 4px 8px;
      border-radius: 6px;
      transition: background 0.2s ease;
    }}
    .photo-open-link:hover {{
      background: rgba(99, 102, 241, 0.1);
    }}

    /* Document Groups */
    .doc-group-card {{
      margin-bottom: 24px;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid var(--glass-border);
      background: var(--glass-bg);
      box-shadow: var(--shadow);
    }}
    .doc-group-head {{
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--glass-border);
      background: rgba(99, 102, 241, 0.04);
      flex-wrap: wrap;
      gap: 10px;
    }}
    .doc-group-title {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.02rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0;
    }}
    .doc-group-count {{
      padding: 3px 10px;
      border-radius: 100px;
      font-size: 0.74rem;
      font-weight: 600;
      background: var(--badge-bg);
      color: var(--text-secondary);
      border: 1px solid var(--badge-border);
    }}
    .doc-group-desc {{
      padding: 10px 20px 4px 20px;
      font-size: 0.82rem;
      color: var(--text-muted);
      margin: 0;
    }}

    /* Empty state */
    .berkas-empty-state {{
      display: none;
      text-align: center;
      padding: 48px 20px;
      color: var(--text-muted);
    }}
    .berkas-empty-state i {{
      width: 48px;
      height: 48px;
      stroke-width: 1.5;
      margin-bottom: 12px;
      opacity: 0.6;
    }}
    .berkas-empty-state h3 {{
      font-size: 1.1rem;
      color: var(--text-primary);
      margin-bottom: 6px;
    }}
    .berkas-empty-state p {{
      font-size: 0.85rem;
      max-width: 420px;
      margin: 0 auto;
    }}
  </style>
</head>
<body>
  <div id="page-loader"><div class="loader-ring"></div></div>
  <div class="bg-wrap">
    <div class="orb o1"></div>
    <div class="orb o2"></div>
    <div class="orb o3"></div>
  </div>

  <nav id="navbar">
    <div class="container nav-inner">
      <a class="nav-logo" href="index.html" style="display:flex; align-items:center;">
        <img src="files/foto/logo/logo.webp" alt="E-Portfolio Logo" style="height:45px; width:auto;">
      </a>
      <ul class="nav-links" id="navList">
        <li><a href="index.html">Beranda</a></li>
        <li><a href="profil.html">Profil</a></li>
        <li><a href="model-guru.html">Model Guru</a></li>
        <li class="dropdown">
          <a href="#" class="dropbtn" style="display:flex; align-items:center; gap:4px;">Semester 1 <i data-lucide="chevron-down" style="width:16px; height:16px;"></i></a>
          <div class="dropdown-content">
            <a href="filosofi-pendidikan.html">Filosofi Pendidikan dan Pendidikan Nilai</a>
            <a href="peserta-didik.html">Peserta didik dan Pemahamannya</a>
            <a href="pembelajaran-mendalam.html">Pembelajaran Mendalam dan Asesmen Dasar</a>
            <a href="artefak.html">Praktik Pengalaman Lapangan (PPL) Terbimbing</a>
            <a href="growth-mindset.html">Pola Pikir Bertumbuh (Growth Mindset)</a>
            <a href="computational-thinking.html">Computational Thinking</a>
          </div>
        </li>
        <li class="dropdown">
          <a href="#" class="dropbtn" style="display:flex; align-items:center; gap:4px;">Semester 2 <i data-lucide="chevron-down" style="width:16px; height:16px;"></i></a>
          <div class="dropdown-content">
            <a href="pembelajaran-sosial-emosional.html">Pembelajaran Sosial Emosional</a>
            <a href="ppl-mandiri.html">Praktik Pengalaman Lapangan (PPL) Mandiri</a>
            <a href="pembelajaran-mendalam-lanjut.html">Pembelajaran Mendalam dan Asesmen Lanjut</a>
            <a href="etika-dan-profesionalisme-guru.html">Etika Dan Profesionalisme Guru</a>
            <a href="projek-kepemimpinan.html">Projek Kepemimpinan</a>
            <a href="seminar-pendidikan-profesi-guru.html">Seminar Pendidikan Profesi Guru</a>
          </div>
        </li>
        <li><a href="berkas.html" class="active">Berkas</a></li>
      </ul>
      <div class="nav-right">
        <button class="theme-btn" id="themeBtn" aria-label="Ubah Tema">
          <i data-lucide="moon"></i>
        </button>
        <button class="hamburger" id="hamburger" aria-label="Buka Menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>

  <div class="page-wrap">
    <section>
      <div class="container">
        <!-- Hero Header -->
        <div class="sec-header fade-in">
          <span class="sec-tag">Dokumen &amp; Multimedia</span>
          <h1 class="sec-title">Pusat Berkas &amp; Multimedia</h1>
          <p class="sec-desc">
            Pusat repositori lengkap seluruh berkas dokumen perkuliahan, modul pembelajaran, lembar kerja, dokumentasi foto, serta rekaman video praktik PPL PPG Prajabatan.
          </p>
          <div class="divider"></div>
        </div>

        <!-- Stat Counter Cards -->
        <div class="berkas-stat-grid fade-in">
          <div class="glass berkas-stat-card">
            <div class="berkas-stat-icon stat-blue">
              <i data-lucide="file-text"></i>
            </div>
            <div>
              <div class="berkas-stat-val">{total_docs}</div>
              <div class="berkas-stat-lbl">Dokumen &amp; Modul Ajar</div>
            </div>
          </div>
          <div class="glass berkas-stat-card">
            <div class="berkas-stat-icon stat-purple">
              <i data-lucide="camera"></i>
            </div>
            <div>
              <div class="berkas-stat-val">{len(photos)}</div>
              <div class="berkas-stat-lbl">Foto Dokumentasi Kegiatan</div>
            </div>
          </div>
          <div class="glass berkas-stat-card">
            <div class="berkas-stat-icon stat-red">
              <i data-lucide="video"></i>
            </div>
            <div>
              <div class="berkas-stat-val">{len(videos)}</div>
              <div class="berkas-stat-lbl">Video Praktik Mengajar</div>
            </div>
          </div>
          <div class="glass berkas-stat-card">
            <div class="berkas-stat-icon stat-emerald">
              <i data-lucide="graduation-cap"></i>
            </div>
            <div>
              <div class="berkas-stat-val">12</div>
              <div class="berkas-stat-lbl">Mata Kuliah &amp; Program PPL</div>
            </div>
          </div>
        </div>

        <!-- Global Live Search -->
        <div class="berkas-search-box fade-in">
          <i data-lucide="search" class="berkas-search-icon"></i>
          <input
            type="text"
            id="berkasGlobalSearch"
            placeholder="Cari nama berkas, modul ajar, foto, video, atau topik perkuliahan..."
            class="berkas-search-input"
            autocomplete="off"
          />
          <button type="button" id="clearSearchBtn" class="berkas-clear-search" title="Hapus pencarian">
            <i data-lucide="x" style="width: 16px; height: 16px;"></i>
          </button>
        </div>

        <!-- Main Category Tabs -->
        <div class="berkas-tabs fade-in">
          <button class="berkas-tab active" data-target="tab-foto">
            <i data-lucide="camera" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 7px;"></i>
            Foto Dokumentasi ({len(photos)})
          </button>
          <button class="berkas-tab" data-target="tab-video">
            <i data-lucide="video" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 7px;"></i>
            Video Praktik ({len(videos)})
          </button>
          <button class="berkas-tab" data-target="tab-dokumen">
            <i data-lucide="folder-open" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 7px;"></i>
            Dokumen Perkuliahan ({total_docs})
          </button>
          <button class="berkas-tab" data-target="tab-all-media">
            <i data-lucide="layers" style="width: 15px; height: 15px; vertical-align: middle; margin-right: 7px;"></i>
            Ringkasan Berkas
          </button>
        </div>

        <!-- ════════ TAB 1: FOTO DOKUMENTASI ════════ -->
        <div class="berkas-pane active" id="tab-foto">
          <!-- Filter Pills -->
          <div class="filter-pills-wrap fade-in">
            <button class="filter-pill active" data-filter="all">
              <i data-lucide="grid" style="width: 14px; height: 14px;"></i> Semua Foto ({len(photos)})
            </button>
            <button class="filter-pill" data-filter="ppl-mandiri">
              <i data-lucide="camera" style="width: 14px; height: 14px;"></i> PPL Mandiri (13)
            </button>
            <button class="filter-pill" data-filter="non-mengajar">
              <i data-lucide="award" style="width: 14px; height: 14px;"></i> Kegiatan Non Mengajar (6)
            </button>
            <button class="filter-pill" data-filter="ppl-terbimbing">
              <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> PPL Terbimbing (6)
            </button>
            <button class="filter-pill" data-filter="kegiatan-sekolah">
              <i data-lucide="users" style="width: 14px; height: 14px;"></i> Kegiatan Persekolahan (12)
            </button>
          </div>

          <!-- Photo Cards Grid -->
          <div class="photo-gallery-grid" id="photoGalleryGrid">
"""

for p in photos:
    html += f"""            <div class="photo-card-glass searchable-item" data-category="{p['cat_code']}" data-search="{p['title']} {p['category']} {p['tag']} {p['desc']}" onclick="openPhotoLightbox('{p['src']}', '{p['title'].replace("'", "&#39;")}')">
              <div class="photo-card-thumb">
                <img src="{p['src']}" alt="{p['title']}" loading="lazy" onerror="this.onerror=null; this.src='files/foto/logo/logo.webp';">
                <div class="photo-zoom-overlay">
                  <i data-lucide="maximize-2" style="width: 16px; height: 16px;"></i>
                </div>
              </div>
              <div class="photo-card-body">
                <div class="photo-card-head">
                  <span class="photo-tag">{p['tag']}</span>
                  <span class="photo-size">{p.get('size', '')}</span>
                </div>
                <h4 class="photo-card-title">{p['title']}</h4>
                <p class="photo-card-desc">{p['desc']}</p>
                <div class="photo-card-action">
                  <a href="{p['src']}" class="photo-open-link" target="_blank" onclick="event.stopPropagation();">
                    <i data-lucide="external-link" style="width: 13px; height: 13px;"></i> Buka Foto Penuh
                  </a>
                </div>
              </div>
            </div>
"""

html += """          </div>
          <div class="berkas-empty-state" id="photoEmptyState">
            <i data-lucide="image-off"></i>
            <h3>Tidak Ada Foto Ditemukan</h3>
            <p>Tidak ada foto yang cocok dengan kata kunci pencarian Anda. Coba kata kunci yang lain.</p>
          </div>
        </div>

        <!-- ════════ TAB 2: VIDEO PRAKTIK ════════ -->
        <div class="berkas-pane" id="tab-video">
          <div class="video-showcase-grid" id="videoShowcaseGrid">
"""

for v in videos:
    html += f"""            <div class="video-card-glass searchable-item" data-search="{v['title']} {v['subtitle']} {v['category']} {v['desc']} {v['fase']}">
              <div class="video-player-wrap">
                <iframe
                  src="{v['embed']}"
                  title="{v['title']}"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowfullscreen
                  loading="lazy">
                </iframe>
              </div>
              <div class="video-card-body">
                <span class="video-card-tag"><i data-lucide="play-circle" style="width: 13px; height: 13px;"></i> {v['tag']}</span>
                <h3 class="video-card-title">{v['title']}</h3>
                <span class="video-card-subtitle">{v['subtitle']}</span>
                <div class="video-card-meta">
                  <span><i data-lucide="compass" style="width: 13px; height: 13px;"></i> {v['fase']}</span>
                  <span><i data-lucide="map-pin" style="width: 13px; height: 13px;"></i> {v['sekolah']}</span>
                </div>
                <p class="video-card-desc">{v['desc']}</p>
                <div class="video-card-footer">
                  <a href="{v['url']}" target="_blank" class="video-action-btn primary" style="display:inline-flex; align-items:center; gap:6px; padding:8px 16px; font-size:0.84rem; text-decoration:none;">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" style="vertical-align: middle;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg> Tonton di YouTube
                  </a>
                </div>
              </div>
            </div>
"""

html += """          </div>
          <div class="berkas-empty-state" id="videoEmptyState">
            <i data-lucide="video-off"></i>
            <h3>Tidak Ada Video Ditemukan</h3>
            <p>Tidak ada rekaman video yang cocok dengan kata kunci pencarian Anda.</p>
          </div>
        </div>

        <!-- ════════ TAB 3: DOKUMEN PERKULIAHAN ════════ -->
        <div class="berkas-pane" id="tab-dokumen">
          <!-- Document Filter Pills -->
          <div class="filter-pills-wrap fade-in">
            <button class="filter-pill active" data-doc-filter="all">
              <i data-lucide="layers" style="width: 14px; height: 14px;"></i> Semua Dokumen ({total_docs})
            </button>
            <button class="filter-pill" data-doc-filter="ppl-mandiri">
              <i data-lucide="briefcase" style="width: 14px; height: 14px;"></i> PPL Mandiri (16)
            </button>
            <button class="filter-pill" data-doc-filter="ppl-terbimbing">
              <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> PPL Terbimbing (18)
            </button>
            <button class="filter-pill" data-doc-filter="sem2">
              <i data-lucide="calendar" style="width: 14px; height: 14px;"></i> Semester 2 (78)
            </button>
            <button class="filter-pill" data-doc-filter="sem1">
              <i data-lucide="calendar" style="width: 14px; height: 14px;"></i> Semester 1 (61)
            </button>
          </div>

          <div id="docGroupsContainer">
"""

sem2_cats = ["PPL Mandiri (Semester 2)", "Pembelajaran Sosial dan Emosional", "Pembelajaran Mendalam dan Asesmen Lanjut", "Etika dan Profesionalisme Guru", "Projek Kepemimpinan", "Seminar Pendidikan Profesi Guru"]
sem1_cats = ["PPL Terbimbing (Semester 1)", "Filosofi Pendidikan dan Pendidikan Nilai", "Pemahaman tentang Peserta Didik dan Pembelajaran", "Pembelajaran Mendalam dan Asesmen Dasar", "Pola Pikir Bertumbuh (Growth Mindset)", "Computational Thinking"]

for cat_name, cat_data in doc_categories.items():
    code = cat_data["code"]
    sem_tag = "sem2" if cat_name in sem2_cats else "sem1"
    files = cat_data["files"]
    html += f"""            <!-- Group: {cat_name} -->
            <div class="doc-group-card doc-group-section" data-cat="{code}" data-sem="{sem_tag}">
              <div class="doc-group-head">
                <h3 class="doc-group-title">
                  <i data-lucide="folder" style="width: 18px; height: 18px; color: var(--primary-light);"></i>
                  {cat_name}
                </h3>
                <span class="doc-group-count">{len(files)} Berkas</span>
              </div>
              <p class="doc-group-desc">{cat_data['desc']}</p>
              <div class="file-list" style="padding: 12px 18px 18px;">
"""
    for doc in files:
        html += f"""                <a href="{doc['filename']}" class="file-row searchable-item" target="_blank" data-search="{doc['name']} {cat_name} {doc['type']}">
                  <span class="file-row-icon"><i data-lucide="file-text"></i></span>
                  <span class="file-row-info">
                    <strong>{doc['name']}</strong>
                    <span>{cat_name} · Format {doc['type'].upper()} ({doc['size']})</span>
                  </span>
                  <span class="file-row-tag">{doc['type'].upper()}</span>
                </a>
"""
    html += """              </div>
            </div>
"""

html += """          </div>
          <div class="berkas-empty-state" id="docEmptyState">
            <i data-lucide="file-x"></i>
            <h3>Tidak Ada Dokumen Ditemukan</h3>
            <p>Tidak ada berkas perkuliahan yang sesuai dengan kueri pencarian Anda.</p>
          </div>
        </div>

        <!-- ════════ TAB 4: RINGKASAN SEMUA BERKAS (DASHBOARD) ════════ -->
        <div class="berkas-pane" id="tab-all-media">
          <!-- Featured Video Section -->
          <div class="fade-in" style="margin-bottom: 28px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
              <div>
                <span class="sec-tag">Sorotan Video Praktik</span>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin: 4px 0 0;">Rekaman Video PPL Mandiri Siklus 1 - 4</h3>
              </div>
              <button type="button" class="tab-btn" onclick="switchBerkasTab('tab-video')" style="font-size:0.8rem; padding:6px 14px;">
                <i data-lucide="arrow-right" style="width:13px; height:13px; margin-right:4px;"></i> Lihat Semua Video (4)
              </button>
            </div>
            <div class="video-showcase-grid">
"""

# Include the 2 most notable videos in summary
for v in videos[:2]:
    html += f"""              <div class="video-card-glass">
                <div class="video-player-wrap">
                  <iframe src="{v['embed']}" title="{v['title']}" allowfullscreen loading="lazy"></iframe>
                </div>
                <div class="video-card-body">
                  <span class="video-card-tag"><i data-lucide="play-circle" style="width: 13px; height: 13px;"></i> {v['tag']}</span>
                  <h4 class="video-card-title">{v['title']}</h4>
                  <p class="video-card-desc">{v['desc']}</p>
                </div>
              </div>
"""

html += f"""            </div>
          </div>

          <!-- Featured Photo Section -->
          <div class="fade-in" style="margin-bottom: 28px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
              <div>
                <span class="sec-tag">Galeri Foto Unggulan</span>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin: 4px 0 0;">Dokumentasi PPL Mandiri &amp; Non Mengajar</h3>
              </div>
              <button type="button" class="tab-btn" onclick="switchBerkasTab('tab-foto')" style="font-size:0.8rem; padding:6px 14px;">
                <i data-lucide="arrow-right" style="width:13px; height:13px; margin-right:4px;"></i> Lihat Semua Foto ({len(photos)})
              </button>
            </div>
            <div class="photo-gallery-grid">
"""

for p in photos[:4]:
    html += f"""              <div class="photo-card-glass" onclick="openPhotoLightbox('{p['src']}', '{p['title'].replace("'", "&#39;")}')">
                <div class="photo-card-thumb">
                  <img src="{p['src']}" alt="{p['title']}" loading="lazy">
                  <div class="photo-zoom-overlay">
                    <i data-lucide="maximize-2" style="width: 16px; height: 16px;"></i>
                  </div>
                </div>
                <div class="photo-card-body">
                  <div class="photo-card-head">
                    <span class="photo-tag">{p['tag']}</span>
                    <span class="photo-size">{p.get('size', '')}</span>
                  </div>
                  <h4 class="photo-card-title">{p['title']}</h4>
                  <p class="photo-card-desc">{p['desc']}</p>
                </div>
              </div>
"""

html += f"""            </div>
          </div>

          <!-- Quick Access PPL Mandiri Documents -->
          <div class="fade-in">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
              <div>
                <span class="sec-tag">Akses Cepat Modul &amp; LK</span>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin: 4px 0 0;">Perangkat Pembelajaran PPL Mandiri</h3>
              </div>
              <button type="button" class="tab-btn" onclick="switchBerkasTab('tab-dokumen')" style="font-size:0.8rem; padding:6px 14px;">
                <i data-lucide="arrow-right" style="width:13px; height:13px; margin-right:4px;"></i> Buka Arsip Lengkap ({total_docs})
              </button>
            </div>
            <div class="glass file-group" style="margin-bottom: 24px;">
              <div class="file-list" style="padding: 14px 18px;">
"""

for doc in doc_categories["PPL Mandiri (Semester 2)"]["files"][:6]:
    html += f"""                <a href="{doc['filename']}" class="file-row" target="_blank">
                  <span class="file-row-icon"><i data-lucide="file-text"></i></span>
                  <span class="file-row-info">
                    <strong>{doc['name']}</strong>
                    <span>PPL Mandiri · Format {doc['type'].upper()} ({doc['size']})</span>
                  </span>
                  <span class="file-row-tag">{doc['type'].upper()}</span>
                </a>
"""

html += """              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
  </div>

  <footer>
    <p>
      · 2026 <strong>Muhammad Fajrul Fahmi</strong> · E-Portfolio PPL PPG ·
      <a href="index.html">Beranda</a>
    </p>
  </footer>

  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <script src="js/data.js"></script>
  <script src="js/main.js"></script>
  <script>
    function openPhotoLightbox(src, title) {
      if (typeof openLightbox === 'function') {
        openLightbox(src, title);
      } else {
        window.open(src, '_blank');
      }
    }

    function switchBerkasTab(targetId) {
      document.querySelectorAll('.berkas-tab').forEach(b => {
        b.classList.toggle('active', b.dataset.target === targetId);
      });
      document.querySelectorAll('.berkas-pane').forEach(p => {
        p.classList.toggle('active', p.id === targetId);
      });
      window.scrollTo({ top: document.querySelector('.berkas-tabs').offsetTop - 90, behavior: 'smooth' });
    }

    function pageInit() {
      // 1. Main Berkas Tab Switching
      document.querySelectorAll(".berkas-tab").forEach(btn => {
        btn.addEventListener("click", () => {
          document.querySelectorAll(".berkas-tab").forEach(b => b.classList.remove("active"));
          document.querySelectorAll(".berkas-pane").forEach(p => p.classList.remove("active"));
          btn.classList.add("active");
          const target = document.getElementById(btn.dataset.target);
          if (target) {
            target.classList.add("active");
          }
          applySearchFilter();
        });
      });

      // 2. Photo Sub-filters
      document.querySelectorAll("#tab-foto .filter-pill").forEach(pill => {
        pill.addEventListener("click", () => {
          document.querySelectorAll("#tab-foto .filter-pill").forEach(p => p.classList.remove("active"));
          pill.classList.add("active");
          const filter = pill.dataset.filter;
          const cards = document.querySelectorAll("#photoGalleryGrid .photo-card-glass");
          cards.forEach(card => {
            const cat = card.dataset.category;
            if (filter === "all" || cat === filter) {
              card.style.display = "";
            } else {
              card.style.display = "none";
            }
          });
          applySearchFilter();
        });
      });

      // 3. Document Sub-filters
      document.querySelectorAll("#tab-dokumen .filter-pill").forEach(pill => {
        pill.addEventListener("click", () => {
          document.querySelectorAll("#tab-dokumen .filter-pill").forEach(p => p.classList.remove("active"));
          pill.classList.add("active");
          const docFilter = pill.dataset.docFilter;
          const sections = document.querySelectorAll("#docGroupsContainer .doc-group-section");
          sections.forEach(sec => {
            const cat = sec.dataset.cat;
            const sem = sec.dataset.sem;
            if (docFilter === "all") {
              sec.style.display = "";
            } else if (docFilter === "ppl-mandiri" && cat === "ppl-mandiri") {
              sec.style.display = "";
            } else if (docFilter === "ppl-terbimbing" && cat === "ppl-terbimbing") {
              sec.style.display = "";
            } else if (docFilter === "sem2" && sem === "sem2") {
              sec.style.display = "";
            } else if (docFilter === "sem1" && sem === "sem1") {
              sec.style.display = "";
            } else {
              sec.style.display = "none";
            }
          });
          applySearchFilter();
        });
      });

      // 4. Live Search Filtering Across Active Items
      const searchInput = document.getElementById("berkasGlobalSearch");
      const clearBtn = document.getElementById("clearSearchBtn");

      function applySearchFilter() {
        const query = searchInput.value.trim().toLowerCase();
        if (query.length > 0) {
          clearBtn.style.display = "block";
        } else {
          clearBtn.style.display = "none";
        }

        const activePane = document.querySelector(".berkas-pane.active");
        if (!activePane) return;

        let visibleCount = 0;
        const items = activePane.querySelectorAll(".searchable-item");

        items.forEach(item => {
          const text = (item.dataset.search || item.textContent || "").toLowerCase();
          const match = query === "" || text.includes(query);
          
          if (item.classList.contains("photo-card-glass")) {
            const activePill = document.querySelector("#tab-foto .filter-pill.active");
            const filter = activePill ? activePill.dataset.filter : "all";
            const catMatch = filter === "all" || item.dataset.category === filter;
            if (match && catMatch) {
              item.style.display = "";
              visibleCount++;
            } else {
              item.style.display = "none";
            }
          } else if (item.classList.contains("file-row")) {
            // inside document groups
            if (match) {
              item.style.display = "";
              visibleCount++;
            } else {
              item.style.display = "none";
            }
          } else {
            // video cards
            if (match) {
              item.style.display = "";
              visibleCount++;
            } else {
              item.style.display = "none";
            }
          }
        });

        // Hide empty document groups in doc tab
        if (activePane.id === "tab-dokumen") {
          const groups = activePane.querySelectorAll(".doc-group-section");
          let totalGroupMatches = 0;
          groups.forEach(g => {
            const activeFilterPill = document.querySelector("#tab-dokumen .filter-pill.active");
            const filterVal = activeFilterPill ? activeFilterPill.dataset.docFilter : "all";
            const cat = g.dataset.cat;
            const sem = g.dataset.sem;
            let filterPass = (filterVal === "all") || (filterVal === "ppl-mandiri" && cat === "ppl-mandiri") || (filterVal === "ppl-terbimbing" && cat === "ppl-terbimbing") || (filterVal === "sem2" && sem === "sem2") || (filterVal === "sem1" && sem === "sem1");

            const rows = g.querySelectorAll(".file-row");
            let hasVisibleRow = false;
            rows.forEach(r => {
              if (r.style.display !== "none") hasVisibleRow = true;
            });

            if (filterPass && hasVisibleRow) {
              g.style.display = "";
              totalGroupMatches++;
            } else {
              g.style.display = "none";
            }
          });
          const emptyState = document.getElementById("docEmptyState");
          if (emptyState) emptyState.style.display = totalGroupMatches === 0 ? "block" : "none";
        }

        // Empty states for photos & videos
        if (activePane.id === "tab-foto") {
          const emptyState = document.getElementById("photoEmptyState");
          if (emptyState) emptyState.style.display = visibleCount === 0 ? "block" : "none";
        }
        if (activePane.id === "tab-video") {
          const emptyState = document.getElementById("videoEmptyState");
          if (emptyState) emptyState.style.display = visibleCount === 0 ? "block" : "none";
        }
      }

      if (searchInput) {
        searchInput.addEventListener("input", applySearchFilter);
      }
      if (clearBtn) {
        clearBtn.addEventListener("click", () => {
          searchInput.value = "";
          searchInput.focus();
          applySearchFilter();
        });
      }

      if (window.lucide) {
        lucide.createIcons();
      }
    }
  </script>
</body>
</html>"""

with open("berkas.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully written updated berkas.html")

