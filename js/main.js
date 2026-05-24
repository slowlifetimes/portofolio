/* ─── Universal Auto-Animation Engine ──────────────────────────────────── */

// Page Loader
function initLoader() {
  const el = document.getElementById("page-loader");
  if (!el) return;

  const hideLoader = () => {
    setTimeout(() => el.classList.add("out"), 180);
  };

  if (document.readyState === "complete") {
    hideLoader();
  } else {
    window.addEventListener("load", hideLoader);
    // Fallback: guarantee loader disappears after 2 seconds
    setTimeout(hideLoader, 2000);
  }
}

// Theme
const THEME_KEY = "ppl-theme";
function applyTheme(t) {
  document.body.classList.toggle("dark", t === "dark");
  const btn = document.getElementById("themeBtn");
  if (!btn) return;
  btn.innerHTML =
    t === "dark" ? '<i data-lucide="sun"></i>' : '<i data-lucide="moon"></i>';
  if (window.lucide) lucide.createIcons({ nodes: [btn] });
}
function initTheme() {
  const saved = localStorage.getItem(THEME_KEY) || "light";
  applyTheme(saved);
  const btn = document.getElementById("themeBtn");
  if (btn)
    btn.addEventListener("click", () => {
      const next = document.body.classList.contains("dark") ? "light" : "dark";
      localStorage.setItem(THEME_KEY, next);
      applyTheme(next);
    });
}

// Navbar
function initNav() {
  const page = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    if (
      a.getAttribute("href") === page ||
      (page === "" && a.getAttribute("href") === "index.html")
    )
      a.classList.add("active");
  });

  const ham = document.getElementById("hamburger");
  const list = document.getElementById("navList");
  if (!ham || !list) return;

  // Create backdrop
  let backdrop = document.getElementById("navBackdrop");
  if (!backdrop) {
    backdrop = document.createElement("div");
    backdrop.id = "navBackdrop";
    backdrop.className = "nav-backdrop";
    document.body.appendChild(backdrop);
  }

  function openDrawer() {
    list.classList.add("open");
    ham.classList.add("active");
    backdrop.classList.add("show");
    document.body.style.overflow = "hidden";
  }

  function closeDrawer() {
    list.classList.remove("open");
    ham.classList.remove("active");
    backdrop.classList.remove("show");
    document.body.style.overflow = "";
  }

  ham.addEventListener("click", () =>
    list.classList.contains("open") ? closeDrawer() : openDrawer(),
  );
  backdrop.addEventListener("click", closeDrawer);
  list
    .querySelectorAll("a")
    .forEach((a) => a.addEventListener("click", closeDrawer));
}

/* ─── UNIVERSAL AUTO-ANIMATE ENGINE ─── */
function autoAnimate() {
  // Apply grad-text to all section headings
  document
    .querySelectorAll(".sec-title:not(.grad-text)")
    .forEach((el) => el.classList.add("grad-text"));
  document
    .querySelectorAll(".siklus-title:not(.grad-text)")
    .forEach((el) => el.classList.add("grad-text"));
  document
    .querySelectorAll(".siklus-card-title:not(.grad-text)")
    .forEach((el) => el.classList.add("grad-text"));
  document
    .querySelectorAll(".misi-card h3:not(.grad-text)")
    .forEach((el) => el.classList.add("grad-text"));

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add("in");
        io.unobserve(e.target);
      });
    },
    { threshold: 0.08, rootMargin: "0px 0px -30px 0px" },
  );

  const obs = (el) => {
    io.observe(el);
  };

  // Section headers
  document.querySelectorAll(".sec-tag:not([data-ae])").forEach((el) => {
    el.classList.add("anim-tag");
    el.dataset.ae = 1;
    obs(el);
  });
  document.querySelectorAll(".sec-title:not([data-ae])").forEach((el) => {
    el.classList.add("anim-title");
    el.style.setProperty("--d", ".05s");
    el.dataset.ae = 1;
    obs(el);
  });
  document.querySelectorAll(".sec-desc:not([data-ae])").forEach((el) => {
    el.classList.add("anim-desc");
    el.style.setProperty("--d", ".15s");
    el.dataset.ae = 1;
    obs(el);
  });
  document.querySelectorAll(".divider:not([data-ae])").forEach((el) => {
    el.classList.add("anim-divider");
    el.style.setProperty("--d", ".2s");
    el.dataset.ae = 1;
    obs(el);
  });

  // Glass cards with stagger
  document
    .querySelectorAll(
      ".glass:not([data-ae]):not(.profile-sidebar):not(.profile-main)",
    )
    .forEach((el, i) => {
      el.classList.add("anim-card");
      el.style.setProperty("--d", `${Math.min(i * 0.06, 0.45)}s`);
      el.dataset.ae = 1;
      obs(el);
    });
  document.querySelectorAll(".profile-sidebar:not([data-ae])").forEach((el) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", ".05s");
    el.dataset.ae = 1;
    obs(el);
  });
  document.querySelectorAll(".profile-main:not([data-ae])").forEach((el) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", ".15s");
    el.dataset.ae = 1;
    obs(el);
  });

  // Badges
  document.querySelectorAll(".badge:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-item");
    el.style.setProperty("--d", `${i * 0.07}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Theory tags
  document.querySelectorAll(".theory-tag:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-item");
    el.style.setProperty("--d", `${i * 0.05}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Nav cards
  document.querySelectorAll(".nav-card:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", `${i * 0.08}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Guru cards
  document.querySelectorAll(".guru-card:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", `${i * 0.12}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Guru card icons
  document.querySelectorAll(".guru-icon:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-icon");
    el.style.setProperty("--d", `${0.1 + i * 0.12}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Roadmap items
  document
    .querySelectorAll(
      '[style*="roadmap"]:not([data-ae]), .roadmap-item:not([data-ae])',
    )
    .forEach((el, i) => {
      el.classList.add("anim-card");
      el.style.setProperty("--d", `${i * 0.1}s`);
      el.dataset.ae = 1;
      obs(el);
    });

  // Table rows
  document
    .querySelectorAll(".score-table tbody tr:not([data-ae])")
    .forEach((el, i) => {
      el.classList.add("anim-row");
      el.style.setProperty("--d", `${i * 0.06}s`);
      el.dataset.ae = 1;
      obs(el);
    });

  // File rows
  document.querySelectorAll(".file-row:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-row");
    el.style.setProperty("--d", `${i * 0.07}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Berkas items
  document.querySelectorAll(".berkas-item:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", `${i * 0.06}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Tab buttons
  document
    .querySelectorAll(".tab-btn:not([data-ae]), .berkas-tab:not([data-ae])")
    .forEach((el, i) => {
      el.classList.add("anim-item");
      el.style.setProperty("--d", `${i * 0.07}s`);
      el.dataset.ae = 1;
      obs(el);
    });

  // Catatan boxes
  document.querySelectorAll(".catatan-box:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", `${i * 0.1}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Score badges
  document.querySelectorAll(".sb:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-item");
    el.style.setProperty("--d", `${i * 0.04}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Map legend items
  document.querySelectorAll(".legend-item:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-item");
    el.style.setProperty("--d", `${i * 0.12}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Section notes
  document.querySelectorAll(".section-note:not([data-ae])").forEach((el) => {
    el.classList.add("anim-desc");
    el.dataset.ae = 1;
    obs(el);
  });

  // Quote block
  document.querySelectorAll(".quote-block:not([data-ae])").forEach((el) => {
    el.classList.add("anim-row");
    el.style.setProperty("--d", ".15s");
    el.dataset.ae = 1;
    obs(el);
  });

  // Misi card
  document.querySelectorAll(".misi-card:not([data-ae])").forEach((el) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", ".05s");
    el.dataset.ae = 1;
    obs(el);
  });

  // Profile stats
  document.querySelectorAll(".p-stats>div:not([data-ae])").forEach((el, i) => {
    el.classList.add("anim-item");
    el.style.setProperty("--d", `${i * 0.12}s`);
    el.dataset.ae = 1;
    obs(el);
  });

  // Map section
  document.querySelectorAll(".map-card:not([data-ae])").forEach((el) => {
    el.classList.add("anim-card");
    el.style.setProperty("--d", ".1s");
    el.dataset.ae = 1;
    obs(el);
  });

  // PDF viewers
  document
    .querySelectorAll(
      ".pdf-frame-wrap:not([data-ae]), .pdf-viewer:not([data-ae])",
    )
    .forEach((el, i) => {
      el.classList.add("anim-card");
      el.style.setProperty("--d", `${i * 0.1}s`);
      el.dataset.ae = 1;
      obs(el);
    });
}

// Re-run autoAnimate for dynamically added elements
function reAnimate() {
  setTimeout(autoAnimate, 50);
}

// Fade-in (legacy)
function initFade() {
  const obs = new IntersectionObserver(
    (e) => {
      e.forEach((x) => {
        if (x.isIntersecting) x.target.classList.add("visible");
      });
    },
    { threshold: 0.08 },
  );
  document.querySelectorAll(".fade-in").forEach((el) => obs.observe(el));
}

// Hero sequential animation
function initHeroAnims() {
  const badge = document.querySelector(".hero-badge");
  const title = document.querySelector(".hero-title");
  const sub = document.querySelector(".hero-sub");
  const desc = document.querySelector(".hero-desc");
  const cta = document.querySelector(".hero-cta");
  const img = document.querySelector(".hero-img, .hero-img-wrap");
  [badge, title, sub, desc, cta].forEach((el, i) => {
    if (el) el.classList.add(`hero-anim-${i + 1}`);
  });
  if (img) img.classList.add("hero-anim-r");
}

// Word reveal
function animateWords(el, baseDelay = 0) {
  if (!el || el.dataset.animated) return;
  el.dataset.animated = "1";
  const text = el.textContent;
  const words = text.trim().split(/\s+/);
  el.innerHTML = words
    .map(
      (w, i) =>
        `<span class="word-wrap"><span class="word-inner" style="animation-delay:${(baseDelay + i * 0.042).toFixed(3)}s">${w}</span></span>${i < words.length - 1 ? " " : ""}`,
    )
    .join("");
}
function initWordAnimations() {
  const obs = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          animateWords(e.target);
          obs.unobserve(e.target);
        }
      });
    },
    { threshold: 0.2 },
  );
  document.querySelectorAll("[data-words]").forEach((el) => obs.observe(el));
}

// Typing cursor for quote
function initTypingQuote() {
  const quote = document.querySelector(".quote-block p");
  if (!quote) return;
  const full = quote.textContent;
  quote.textContent = "";
  const cursor = document.createElement("span");
  cursor.className = "typing-cursor";
  quote.appendChild(cursor);
  let i = 0;
  const type = () => {
    if (i < full.length) {
      cursor.insertAdjacentText("beforebegin", full[i++]);
      setTimeout(type, 26 + Math.random() * 16);
    }
  };
  const obs = new IntersectionObserver(
    ([e]) => {
      if (e.isIntersecting) {
        type();
        obs.disconnect();
      }
    },
    { threshold: 0.5 },
  );
  obs.observe(quote);
}

// Counter animation
function animateCounter(el, target, duration = 1200) {
  const start = performance.now();
  const update = (now) => {
    const p = Math.min((now - start) / duration, 1);
    const ease = 1 - Math.pow(1 - p, 3);
    el.textContent = Math.round(target * ease);
    if (p < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}
function initCounters() {
  const obs = new IntersectionObserver(
    ([e]) => {
      if (e.isIntersecting) {
        document
          .querySelectorAll("[data-count]")
          .forEach((el) => animateCounter(el, parseFloat(el.dataset.count)));
        obs.disconnect();
      }
    },
    { threshold: 0.5 },
  );
  const t = document.querySelector(".p-stats");
  if (t) obs.observe(t);
}

// Score bars
function initScoreBars() {
  const bars = document.querySelectorAll(".score-bar");
  if (!bars.length) return;
  const obs = new IntersectionObserver(
    ([e]) => {
      if (e.isIntersecting) {
        bars.forEach((b, i) => {
          b.style.setProperty("--d", `${i * 0.08}s`);
          b.classList.add("go");
        });
        obs.disconnect();
      }
    },
    { threshold: 0.3 },
  );
  obs.observe(bars[0].closest("table") || bars[0].parentElement);
}

// Generic tabs
function initTabs(tabSel, paneSel) {
  document.querySelectorAll(tabSel).forEach((btn) => {
    btn.addEventListener("click", () => {
      document
        .querySelectorAll(tabSel)
        .forEach((b) => b.classList.remove("active"));
      document
        .querySelectorAll(paneSel)
        .forEach((p) => p.classList.remove("active"));
      btn.classList.add("active");
      const t = document.getElementById(btn.dataset.target);
      if (t) {
        t.classList.add("active");
        setTimeout(autoAnimate, 30);
      }
    });
  });
}

// Page entry
function initPageEntry() {
  document.querySelector(".page-wrap")?.classList.add("page-enter");
}

// File helpers
const FILE_ICONS = {
  pdf: "file-text",
  pptx: "presentation",
  xlsx: "table-2",
  video: "video",
  mp4: "video",
  default: "file",
};
function fileIconName(t) {
  return FILE_ICONS[t] || FILE_ICONS.default;
}
function refreshIcons(el) {
  if (window.lucide) lucide.createIcons({ nodes: el ? [el] : undefined });
}

async function fileExists(url) {
  if (window.location.protocol === "file:") return true; // Local file:// protocol compatibility
  try {
    const r = await fetch(url, { method: "HEAD" });
    if (r.ok) return true;
    const r2 = await fetch(url, { method: "GET" });
    return r2.ok;
  } catch {
    return false;
  }
}

// Global Image Error Handlers for robust offline and local testing
window.handleImageError = function (img, name, size) {
  const row = img.closest(".file-row");
  if (row) {
    row.classList.remove("file-row-img");
    row.classList.add("berkas-unavail");
    row.href = "#";
    row.innerHTML = `
      <span class="file-row-icon"><i data-lucide="image-off"></i></span>
      <span class="file-row-info"><strong>${name}</strong>
      <span>${size ? size + " · " : ""}<em>Belum tersedia</em></span></span>
      <span class="file-row-tag">IMAGE</span>`;
    if (window.lucide) lucide.createIcons({ nodes: [row] });
  }
};

window.handleBerkasImageError = function (img, name, size) {
  const item = img.closest(".berkas-item");
  if (item) {
    item.classList.remove("berkas-item-img");
    item.classList.add("berkas-unavail");
    item.href = "#";
    item.innerHTML = `
      <span class="berkas-item-icon"><i data-lucide="image-off"></i></span>
      <span class="berkas-item-info"><h4>${name}</h4>
      <small>${size ? size + " · " : ""}Belum tersedia</small></span>`;
    if (window.lucide) lucide.createIcons({ nodes: [item] });
  }
};

// Utility to format ISO Date (YYYY-MM-DD) into Indonesian Date (e.g., "10 September 2026")
function formatIndonesianDate(dateStr) {
  if (!dateStr) return "";
  const parts = dateStr.split("-");
  if (parts.length !== 3) return dateStr;

  const year = parts[0];
  const month = parseInt(parts[1], 10);
  const day = parseInt(parts[2], 10);

  const months = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
  ];

  if (month < 1 || month > 12) return dateStr;
  return `${day} ${months[month - 1]} ${year}`;
}

async function renderFileRows(files, container, base = "files/", limit = null) {
  if (!container || !files) return;
  container.innerHTML = "";

  const hasLimit = limit && files.length > limit;

  // Clean up any existing show-all button wrapper for this container
  const existingBtn = container.parentNode.querySelector(".show-all-wrap");
  if (existingBtn) {
    existingBtn.remove();
  }

  let index = 0;
  for (const f of files) {
    const isImage = ["jpg", "jpeg", "png", "webp"].includes(
      f.type.toLowerCase(),
    );
    const url = f.youtube || base + f.filename;
    const ok = f.youtube ? true : await fileExists(url);

    const a = document.createElement("a");
    a.className = "file-row" + (ok ? "" : " berkas-unavail");
    if (isImage) a.classList.add("file-row-img");

    if (hasLimit && index >= limit) {
      a.classList.add("extra-file-row");
      a.classList.add("hidden-row");
      a.style.opacity = "0";
      a.style.transform = "translateY(20px)";
      a.style.transition = "opacity 0.4s ease, transform 0.4s ease";
    }

    a.href = ok ? url : "#";
    a.target = "_blank";
    a.rel = "noopener";

    if (isImage && ok) {
      a.innerHTML = `
        <div class="file-preview-img">
          <img src="${url}" alt="${f.name}" loading="lazy" onerror="handleImageError(this, '${f.name}', '${f.size || ""}')">
        </div>
        <span class="file-row-info">
          <strong>${f.name}</strong>
          <span>Lihat Gambar</span>
        </span>
        <span class="file-row-tag img-tag">IMAGE</span>`;
    } else {
      const formattedDate = formatIndonesianDate(f.date);
      a.innerHTML = `<span class="file-row-icon"><i data-lucide="${fileIconName(f.type)}"></i></span>
        <span class="file-row-info"><strong>${f.name}</strong>
        <span>${formattedDate}${ok ? "" : (formattedDate ? " · " : "") + "<em>Belum tersedia</em>"}</span></span>
        <span class="file-row-tag">${f.type.toUpperCase()}</span>`;
    }
    container.appendChild(a);
    index++;
  }

  if (hasLimit) {
    const extraCount = files.length - limit;
    const wrap = document.createElement("div");
    wrap.className = "show-all-wrap fade-in visible";

    wrap.innerHTML = `
      <button class="show-all-btn glass glass-hover">
        <i data-lucide="image" style="width: 16px; height: 16px;"></i>
        Buka Semua Foto (+${extraCount})
      </button>
    `;

    container.parentNode.appendChild(wrap);

    const btn = wrap.querySelector(".show-all-btn");
    let isExpanded = false;
    
    btn.addEventListener("click", () => {
      const extras = container.querySelectorAll(".extra-file-row");
      if (!isExpanded) {
        // Expand state
        extras.forEach((el, idx) => {
          el.classList.remove("hidden-row");
          el.offsetHeight; // trigger layout reflow
          setTimeout(() => {
            el.style.opacity = "1";
            el.style.transform = "translateY(0)";
          }, idx * 40);
        });

        btn.innerHTML = `
          <i data-lucide="eye-off" style="width: 16px; height: 16px;"></i>
          Sembunyikan Foto
        `;
        refreshIcons(btn);
        isExpanded = true;
      } else {
        // Collapse state
        extras.forEach((el) => {
          el.style.opacity = "0";
          el.style.transform = "translateY(20px)";
          setTimeout(() => {
            el.classList.add("hidden-row");
          }, 400);
        });

        // Smooth scroll back to container to keep context
        container.scrollIntoView({ behavior: "smooth", block: "nearest" });

        btn.innerHTML = `
          <i data-lucide="image" style="width: 16px; height: 16px;"></i>
          Buka Semua Foto (+${extraCount})
        `;
        refreshIcons(btn);
        isExpanded = false;
      }
    });
    refreshIcons(wrap);
  }

  refreshIcons(container);
  reAnimate();
}

async function renderBerkasGrid(files, container, base = "files/") {
  if (!container || !files) return;
  container.innerHTML = "";
  for (const f of files) {
    const isImage = ["jpg", "jpeg", "png", "webp"].includes(
      f.type.toLowerCase(),
    );
    const url = f.youtube || base + f.filename;
    const ok = f.youtube ? true : await fileExists(url);

    const a = document.createElement("a");
    a.className =
      "berkas-item glass glass-hover" + (ok ? "" : " berkas-unavail");
    if (isImage) a.classList.add("berkas-item-img");

    a.href = ok ? url : "#";
    a.target = "_blank";
    a.rel = "noopener";

    if (isImage && ok) {
      a.innerHTML = `
        <div class="berkas-preview-img">
          <img src="${url}" alt="${f.name}" loading="lazy" onerror="handleBerkasImageError(this, '${f.name}', '${f.size || ""}')">
        </div>
        <span class="berkas-item-info"><h4>${f.name}</h4><small>Buka Gambar</small></span>`;
    } else {
      const formattedDate = formatIndonesianDate(f.date);
      a.innerHTML = `<span class="berkas-item-icon"><i data-lucide="${fileIconName(f.type)}"></i></span>
        <span class="berkas-item-info"><h4>${f.name}</h4>
        <small>${f.size || ""}${formattedDate ? " · " + formattedDate : ""}${ok ? "" : " · Belum tersedia"}</small></span>`;
    }
    container.appendChild(a);
  }
  refreshIcons(container);
  reAnimate();
}

async function loadManifest() {
  return typeof PPL_DATA !== "undefined" ? PPL_DATA : { siklus: [] };
}

// ─── INIT ───────────────────────────────────────────────────────────────────
// Mobile Swipe Navigation + Floating Nav Buttons
function initSwipeNav() {
  if (window.innerWidth > 768) return;

  const PAGES = [
    { file: "index.html", label: "Beranda" },
    { file: "profil.html", label: "Profil" },
    { file: "artefak.html", label: "Artefak" },
    { file: "penilaian.html", label: "Penilaian" },
    { file: "model-guru.html", label: "Model Guru" },
    { file: "berkas.html", label: "Berkas" },
  ];

  const currentPage = location.pathname.split("/").pop() || "index.html";
  const currentIdx = PAGES.findIndex((p) => p.file === currentPage);
  if (currentIdx === -1) return;

  function navigate(idx) {
    document.body.style.transition = "opacity 0.25s";
    document.body.style.opacity = "0";
    setTimeout(() => {
      location.href = PAGES[idx].file;
    }, 240);
  }

  // ── Floating arrow buttons ──
  function makeArrow(id, points) {
    const btn = document.createElement("button");
    btn.id = id;
    btn.setAttribute(
      "aria-label",
      id === "pnb-prev" ? "Halaman sebelumnya" : "Halaman berikutnya",
    );
    btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"
      fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="${points}"/></svg>`;
    document.body.appendChild(btn);
    return btn;
  }

  const prevBtn =
    currentIdx > 0 ? makeArrow("pnb-prev", "15 18 9 12 15 6") : null;
  const nextBtn =
    currentIdx < PAGES.length - 1
      ? makeArrow("pnb-next", "9 18 15 12 9 6")
      : null;
  if (prevBtn)
    prevBtn.addEventListener("click", () => navigate(currentIdx - 1));
  if (nextBtn)
    nextBtn.addEventListener("click", () => navigate(currentIdx + 1));

  // Swipe navigation disabled to prevent scroll and navigation conflicts on mobile layout
  /*
  // ── Swipe detection ──
  const IGNORE_SELECTORS =
    ".tab-nav, .berkas-tabs, .nav-links, [data-no-swipe]";
  let touchStartX = 0,
    touchStartY = 0,
    swiping = false;

  document.addEventListener(
    "touchstart",
    (e) => {
      if (e.target.closest(IGNORE_SELECTORS)) {
        swiping = false;
        return;
      }
      touchStartX = e.touches[0].clientX;
      touchStartY = e.touches[0].clientY;
      swiping = true;
    },
    { passive: true },
  );

  document.addEventListener(
    "touchend",
    (e) => {
      if (!swiping) return;
      const dx = e.changedTouches[0].clientX - touchStartX;
      const dy = e.changedTouches[0].clientY - touchStartY;
      if (Math.abs(dx) < 60 || Math.abs(dy) > 120) return;
      if (dx < 0 && currentIdx < PAGES.length - 1) navigate(currentIdx + 1);
      if (dx > 0 && currentIdx > 0) navigate(currentIdx - 1);
    },
    { passive: true },
  );
  */
}

// Premium Glassmorphic Lightbox Modal Manager
function openLightbox(src, title) {
  let modal = document.getElementById("lightboxModal");
  if (!modal) {
    modal = document.createElement("div");
    modal.id = "lightboxModal";
    modal.className = "lightbox-modal";
    modal.innerHTML = `
      <div class="lightbox-close" id="lightboxClose">&times;</div>
      <div class="lightbox-content">
        <img id="lightboxImg" src="" alt="Lightbox Image">
        <div class="lightbox-title" id="lightboxTitle"></div>
      </div>
    `;
    document.body.appendChild(modal);

    modal.addEventListener("click", (e) => {
      if (e.target === modal || e.target.id === "lightboxClose") {
        closeLightbox();
      }
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeLightbox();
    });
  }

  const lightboxImg = document.getElementById("lightboxImg");
  const lightboxTitle = document.getElementById("lightboxTitle");
  if (lightboxImg && lightboxTitle) {
    lightboxImg.src = src;
    lightboxTitle.textContent = title;
    modal.classList.add("active");
    document.body.style.overflow = "hidden";
  }
}

function closeLightbox() {
  const modal = document.getElementById("lightboxModal");
  if (modal) {
    modal.classList.remove("active");
    document.body.style.overflow = "";
  }
}

// Global click delegation for photo cards
document.addEventListener("click", (e) => {
  const fileRowImg = e.target.closest(".file-row-img, .berkas-item-img");
  if (fileRowImg && !fileRowImg.classList.contains("berkas-unavail")) {
    e.preventDefault();
    const img = fileRowImg.querySelector("img");
    const title =
      (fileRowImg.querySelector("strong") || fileRowImg.querySelector("h4"))
        ?.textContent || "Dokumentasi";
    if (img && img.src) {
      openLightbox(img.src, title);
    }
  }
});

// Premium Glassmorphic PDF Modal Viewer Manager
function openPdfModal(src, title) {
  let modal = document.getElementById("pdfModal");
  if (!modal) {
    modal = document.createElement("div");
    modal.id = "pdfModal";
    modal.className = "pdf-modal";
    modal.innerHTML = `
      <div class="pdf-modal-content">
        <div class="pdf-modal-header">
          <span class="pdf-modal-title" id="pdfModalTitle"></span>
          <button class="pdf-modal-close" id="pdfModalClose">&times;</button>
        </div>
        <div class="pdf-modal-body">
          <iframe id="pdfModalFrame" src="" allow="autoplay"></iframe>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    modal.addEventListener("click", (e) => {
      if (e.target === modal || e.target.id === "pdfModalClose") {
        closePdfModal();
      }
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closePdfModal();
    });
  }

  const pdfFrame = document.getElementById("pdfModalFrame");
  const pdfTitle = document.getElementById("pdfModalTitle");
  if (pdfFrame && pdfTitle) {
    pdfFrame.src = src;
    pdfTitle.textContent = title;
    modal.classList.add("active");
    document.body.style.overflow = "hidden";
  }
}

function closePdfModal() {
  const modal = document.getElementById("pdfModal");
  if (modal) {
    modal.classList.remove("active");
    const pdfFrame = document.getElementById("pdfModalFrame");
    if (pdfFrame) pdfFrame.src = ""; // Clear iframe src to stop background audio/loads
    document.body.style.overflow = "";
  }
}

// Global click delegation for PDF links
document.addEventListener("click", (e) => {
  const fileLink = e.target.closest(".file-row, .berkas-item");
  if (fileLink && !fileLink.classList.contains("berkas-unavail")) {
    const url = fileLink.getAttribute("href");
    if (url && url.toLowerCase().endsWith(".pdf")) {
      // On mobile view (<= 768px), allow the PDF to open directly in a new tab natively
      // to avoid broken iframe renderings and make it instantly viewable.
      if (window.innerWidth <= 768) {
        return;
      }
      e.preventDefault();
      const title =
        fileLink.querySelector("strong, h4")?.textContent || "Dokumen PDF";
      openPdfModal(url, title);
    }
  }
});

document.addEventListener("DOMContentLoaded", () => {
  initLoader();
  initTheme();
  initNav();
  initFade();
  initPageEntry();
  initHeroAnims();
  initWordAnimations();
  initCounters();
  initScoreBars();
  initTypingQuote();
  initSwipeNav();
  if (window.lucide) lucide.createIcons();
  // Run auto-animate after a short delay so Lucide icons are rendered
  setTimeout(autoAnimate, 80);
  if (typeof pageInit === "function") pageInit();
});
