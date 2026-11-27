# Why it's built this way

A personal engineering site has two jobs: state clearly who I am and what I deliver, and point to evidence a reviewer can inspect. It should load immediately, remain accessible on any viewport, and stay cheap to keep accurate.

## Design choices

**Why plain HTML with no build step?** Because the site is a compact set of stable pages. A static site generator adds toolchain maintenance without helping readers. GitHub Pages serves static files directly, so what lives in the repository is exactly what browsers receive.

**Why no client-side JavaScript?** Navigation, responsive layout, light and dark colour schemes, and inline architecture diagrams work purely in HTML and CSS. No interactive scripts means zero script execution surface, zero bundle cost, and instant first paint. (Structured Schema.org metadata uses standard non-executable `<script type="application/ld+json">` blocks.)

**Why no analytics or trackers?** Readers should not be tracked across essays. A raw visit count measures clicks, not accuracy or usefulness.

**Why system fonts instead of web fonts?** Web fonts add network requests and layout shift. Using native platform sans-serif, serif, and monospace stacks keeps rendering instant and readable offline or on constrained connections.

**Why one stylesheet built on custom properties?** Light and dark schemes share every rule while swapping only colour tokens. Every foreground/background pair is checked to meet or exceed WCAG 2.2 AA (`>= 4.5:1`) contrast, interactive targets meet mobile `>= 44px` tap-height ergonomics, and responsive rules avoid horizontal overflow on `390px` phones and `768px` tablets.

**Why does `404.html` use root-relative links when other pages use relative ones?** Because GitHub Pages serves `404.html` at arbitrary missing sub-paths such as `/writing/missing/page`. Root-relative links ensure assets and navigation resolve from any depth.

**Why a small Python link checker rather than a crawler?** Reading HTML pages and `sitemap.xml` directly from disk runs in milliseconds with only the Python standard library, checks `#fragment` ids and same-site Open Graph URLs, rejects empty link targets, and behaves identically offline and in CI.

**Why pin the `html-validate` version in CI?** Pinning `11.16.1` ensures CI failures reflect changes in the site rather than upstream rule additions.

## Questions worth asking

**Without analytics, how will you know the site works?** By validating every change: `html-validate` checks markup conformance, and `scripts/check_links.py` verifies internal links, anchors, Open Graph URLs, and sitemap targets. Readers can reach out via LinkedIn or GitHub (listed under `#contact`).

**How are claims and citations kept accurate?** Essays cite public sources with clickable links, distinguish synthetic examples and illustrative benchmarks from measured production outcomes, and keep employer-specific operational figures separate from open-source reference work. References to public guidance are my own reading: unofficial and not government guidance.

**Does it hold up for keyboard and screen-reader users?** Each page has a skip link, a single `<header>` (`banner`) and `<main id="main">` landmark, labelled navigation with `aria-current="page"`, visible `:focus-visible` outlines, accessible SVG titles/descriptions, and monotonic headings. Automated `axe-core` checks were run across light and dark schemes at desktop and mobile widths; manual screen-reader verification with VoiceOver and NVDA remains an active next step.

## What comes next

- Run automated `axe-core` accessibility assertions in CI on every pull request alongside HTML validation and link checking.
- Complete manual screen-reader passes in VoiceOver and NVDA and address any friction found.
