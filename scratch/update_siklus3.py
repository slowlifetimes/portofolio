import re

def update_siklus3():
    path = "ppl-mandiri-siklus3.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    doc_start = content.find('<!-- --- TAB: DOKUMENTASI PRAKTIK SIKLUS 3 --- -->')
    if doc_start == -1:
        print("Error: Could not find tab start")
        return

    section_end = content.find('</section>', doc_start)
    if section_end == -1:
        print("Error: Could not find section end")
        return

    old_tab = content[doc_start:section_end]
    print(f"Found old tab block, length: {len(old_tab)}")

    new_tab = """<!-- --- TAB: DOKUMENTASI PRAKTIK SIKLUS 3 --- -->
        <div class="tab-pane" id="dokumentasi">
          <div class="siklus-container">
            <!-- Hero Card -->
            <div class="glass siklus-hero fade-in">
              <span class="sec-tag">Dokumentasi · PPL Mandiri Siklus 3</span>
              <h2 class="siklus-title">
                Dokumentasi Praktik Pembelajaran Siklus 3
              </h2>
              <div class="meta-row">
                <span class="meta-item"><i data-lucide="calendar"></i> Fase D / Kelas VII</span>
                <span class="meta-item"><i data-lucide="map-pin"></i> SMP Negeri 18 Malang</span>
                <span class="meta-item"><i data-lucide="camera"></i> 3 Foto Dokumentasi</span>
              </div>
              <p class="hero-desc">
                Dokumentasi visual pelaksanaan pembelajaran mandiri Siklus 3 di SMP Negeri 18 Malang, mencakup tahap pendahuluan pembelajaran, kegiatan inti penyelidikan langsung komponen hardware CPU berbantuan AI Google Lens, serta pengerjaan LKPD klasifikasi komponen IPOS secara kolaboratif.
              </p>
            </div>

            <!-- Dokumentasi Praktik Siklus 3 Slider -->
            <div class="files-container fade-in">
              <div class="glass file-group">
                <div class="file-group-head">
                  <span><i data-lucide="camera" style="width: 14px; height: 14px; vertical-align: middle; margin-right: 6px;"></i> Galeri Dokumentasi Praktik Siklus 3</span>
                </div>

                <div class="doc-slider-wrap" data-slider="siklus-3">
                  <!-- Slider Viewport -->
                  <div class="doc-slider-viewport">
                    <div class="doc-slider-track">
                      <div class="doc-slider-slide" data-index="0" data-src="files/foto/PPL Mandiri/Siklus 3/Pendahuluan.png" data-title="Tahap Pendahuluan &amp; Apersepsi Pembelajaran" data-desc="Pendahuluan Pembelajaran · Pembukaan, Presensi Siswa, Motivasi &amp; Pengenalan Alur Praktik Hardware Komputer" data-tag="DOKUMEN 1">
                        <img src="files/foto/PPL Mandiri/Siklus 3/Pendahuluan.png" alt="Tahap Pendahuluan &amp; Apersepsi Pembelajaran" loading="lazy">
                      </div>
                      <div class="doc-slider-slide" data-index="1" data-src="files/foto/PPL Mandiri/Siklus 3/Kegiatan Praktik menggunakan Google Lens.png" data-title="Praktik Penyelidikan Hardware Menggunakan Google Lens" data-desc="Kegiatan Inti · Peserta Didik Mengidentifikasi dan Memindai Komponen Hardware Komputer Menggunakan Fitur AI Google Lens" data-tag="DOKUMEN 2">
                        <img src="files/foto/PPL Mandiri/Siklus 3/Kegiatan Praktik menggunakan Google Lens.png" alt="Praktik Penyelidikan Hardware Menggunakan Google Lens" loading="lazy">
                      </div>
                      <div class="doc-slider-slide" data-index="2" data-src="files/foto/PPL Mandiri/Siklus 3/Murid Menjawab LKPD.png" data-title="Pengerjaan LKPD &amp; Pengelompokan Komponen IPOS" data-desc="Aktivitas Belajar · Siswa Mendiskusikan Hasil Pengamatan dan Mengisi LKPD Klasifikasi Komponen IPOS (Input, Process, Output, Storage)" data-tag="DOKUMEN 3">
                        <img src="files/foto/PPL Mandiri/Siklus 3/Murid Menjawab LKPD.png" alt="Pengerjaan LKPD &amp; Pengelompokan Komponen IPOS" loading="lazy">
                      </div>
                    </div>

                    <!-- Counter Badge -->
                    <div class="doc-slider-counter"><span class="cur-num">1</span> / <span class="total-num">3</span></div>

                    <!-- Nav Arrows -->
                    <button class="doc-slider-btn prev" type="button" aria-label="Foto Sebelumnya">
                      <i data-lucide="chevron-left"></i>
                    </button>
                    <button class="doc-slider-btn next" type="button" aria-label="Foto Berikutnya">
                      <i data-lucide="chevron-right"></i>
                    </button>

                    <!-- Caption Overlay -->
                    <div class="doc-slider-caption">
                      <div class="doc-slider-caption-text">
                        <span class="cap-tag">DOKUMEN 1</span>
                        <strong class="cap-title">Tahap Pendahuluan &amp; Apersepsi Pembelajaran</strong>
                        <span class="cap-desc">Pendahuluan Pembelajaran · Pembukaan, Presensi Siswa, Motivasi &amp; Pengenalan Alur Praktik Hardware Komputer</span>
                      </div>
                      <button type="button" class="cap-btn" title="Perbesar Foto (Lightbox)">
                        <i data-lucide="maximize-2"></i>
                      </button>
                    </div>

                    <!-- Dots Indicator -->
                    <div class="doc-slider-dots">
                      <button class="doc-dot active" type="button" aria-label="Slide 1"></button>
                      <button class="doc-dot" type="button" aria-label="Slide 2"></button>
                      <button class="doc-dot" type="button" aria-label="Slide 3"></button>
                    </div>
                  </div>

                  <!-- Clickable Items List -->
                  <div class="doc-slider-items file-list" style="margin-top: 16px;">
                    <a href="files/foto/PPL Mandiri/Siklus 3/Pendahuluan.png" class="file-row active" target="_blank">
                      <span class="file-row-icon"><i data-lucide="image"></i></span>
                      <span class="file-row-info">
                        <strong>1. Tahap Pendahuluan &amp; Apersepsi Pembelajaran</strong>
                        <span>Pendahuluan Kelas, Presensi Kehadiran, Motivasi &amp; Penjelasan Alur Pembelajaran Hardware</span>
                      </span>
                      <span class="file-row-tag">DOKUMEN 1</span>
                    </a>
                    <a href="files/foto/PPL Mandiri/Siklus 3/Kegiatan Praktik menggunakan Google Lens.png" class="file-row" target="_blank">
                      <span class="file-row-icon"><i data-lucide="image"></i></span>
                      <span class="file-row-info">
                        <strong>2. Praktik Penyelidikan Hardware Menggunakan Google Lens</strong>
                        <span>Penyelidikan Langsung Komponen Internal CPU &amp; Penelusuran Informasi Berbasis Google Lens</span>
                      </span>
                      <span class="file-row-tag">DOKUMEN 2</span>
                    </a>
                    <a href="files/foto/PPL Mandiri/Siklus 3/Murid Menjawab LKPD.png" class="file-row" target="_blank">
                      <span class="file-row-icon"><i data-lucide="image"></i></span>
                      <span class="file-row-info">
                        <strong>3. Pengerjaan LKPD &amp; Pengelompokan Komponen IPOS</strong>
                        <span>Diskusi Kelompok, Dokumentasi Komponen &amp; Pengisian Lembar Kerja Peserta Didik (LKPD)</span>
                      </span>
                      <span class="file-row-tag">DOKUMEN 3</span>
                    </a>
                  </div>

                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    """

    content = content[:doc_start] + new_tab + content[section_end:]

    # Also update script block
    script_pattern = r'<script>\s*function pageInit\(\)\s*\{[\s\S]*?\}\s*</script>'
    new_script = """<script>
    function pageInit() {
      initTabs(".tab-btn", ".tab-pane");
      initDocSliders();
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          setTimeout(() => {
            window.dispatchEvent(new Event('resize'));
          }, 60);
        });
      });
    }

    // ── Documentation Image Slider Controller ──
    function initDocSliders() {
      document.querySelectorAll('.doc-slider-wrap').forEach(wrap => {
        const track = wrap.querySelector('.doc-slider-track');
        const slides = wrap.querySelectorAll('.doc-slider-slide');
        const prevBtn = wrap.querySelector('.doc-slider-btn.prev');
        const nextBtn = wrap.querySelector('.doc-slider-btn.next');
        const dots = wrap.querySelectorAll('.doc-dot');
        const curNum = wrap.querySelector('.cur-num');
        const capTag = wrap.querySelector('.cap-tag');
        const capTitle = wrap.querySelector('.cap-title');
        const capDesc = wrap.querySelector('.cap-desc');
        const capBtn = wrap.querySelector('.cap-btn');
        const rows = wrap.querySelectorAll('.doc-slider-items .file-row');
        const viewport = wrap.querySelector('.doc-slider-viewport');

        if (!track || slides.length === 0) return;

        let current = 0;
        const total = slides.length;

        function updateSlide(idx) {
          current = (idx + total) % total;
          track.style.transform = `translateX(-${current * 100}%)`;

          if (curNum) curNum.textContent = current + 1;

          // Dots
          dots.forEach((dot, i) => dot.classList.toggle('active', i === current));

          // Active row
          rows.forEach((row, i) => row.classList.toggle('active', i === current));

          // Caption update
          const curSlide = slides[current];
          if (curSlide) {
            if (capTag) capTag.textContent = curSlide.dataset.tag || `FOTO ${current + 1}`;
            if (capTitle) capTitle.textContent = curSlide.dataset.title || '';
            if (capDesc) capDesc.textContent = curSlide.dataset.desc || '';
          }
        }

        // Open Lightbox Helper
        function triggerLightbox(index) {
          const slide = slides[index];
          if (!slide) return;
          const src = slide.dataset.src;
          const title = slide.dataset.title;
          if (typeof openLightbox === 'function') {
            openLightbox(src, title);
          } else {
            window.open(src, '_blank');
          }
        }

        // Prev & Next
        if (prevBtn) {
          prevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            updateSlide(current - 1);
            resetAuto();
          });
        }

        if (nextBtn) {
          nextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            updateSlide(current + 1);
            resetAuto();
          });
        }

        // Dots click
        dots.forEach((dot, i) => {
          dot.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            updateSlide(i);
            resetAuto();
          });
        });

        // Rows click
        rows.forEach((row, i) => {
          row.addEventListener('click', (e) => {
            e.preventDefault();
            updateSlide(i);
            resetAuto();
          });
        });

        // Slide click & Zoom button -> Lightbox
        slides.forEach((slide, i) => {
          slide.addEventListener('click', () => {
            triggerLightbox(i);
          });
        });

        if (capBtn) {
          capBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            triggerLightbox(current);
          });
        }

        // Touch Swipe
        let startX = 0;
        viewport.addEventListener('touchstart', (e) => {
          startX = e.touches[0].clientX;
        }, { passive: true });

        viewport.addEventListener('touchend', (e) => {
          const dx = e.changedTouches[0].clientX - startX;
          if (Math.abs(dx) > 35) {
            updateSlide(current + (dx < 0 ? 1 : -1));
            resetAuto();
          }
        }, { passive: true });

        // Auto-Play every 5s with pause on hover
        let timer = null;
        function startAuto() {
          if (timer) clearInterval(timer);
          timer = setInterval(() => {
            updateSlide(current + 1);
          }, 5000);
        }

        function stopAuto() {
          if (timer) {
            clearInterval(timer);
            timer = null;
          }
        }

        function resetAuto() {
          stopAuto();
          startAuto();
        }

        viewport.addEventListener('mouseenter', stopAuto);
        viewport.addEventListener('mouseleave', startAuto);

        startAuto();
        updateSlide(0);
      });

      if (window.lucide) {
        lucide.createIcons();
      }
    }
  </script>"""

    content, n = re.subn(script_pattern, new_script, content)
    print(f"Script replaced: {n} times")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated ppl-mandiri-siklus3.html")

update_siklus3()

