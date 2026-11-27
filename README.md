# dsugurtuna.github.io

Source for Ugur Tuna's engineering portfolio and writing site: [dsugurtuna.github.io](https://dsugurtuna.github.io).

Plain HTML and one stylesheet. No build step, no client-side JavaScript framework, no trackers, no web fonts, and no third-party CDNs. GitHub Pages serves the files directly from `main`.

## Structure

```text
.
├── index.html                  Home: dual-track positioning, verified track record,
│                               focus areas, career arc, selected systems, writing, connect
├── projects.html               Systems & reference architectures showcase (7 public repos)
├── writing/
│   ├── index.html              Essay index
│   ├── feed.xml                RSS / Atom feed
│   ├── usage-is-not-quality.html
│   ├── read-freely-write-carefully.html
│   ├── a-second-model-is-a-critic.html
│   ├── cheap-models-are-expensive.html
│   ├── a-partner-not-a-button.html
│   ├── write-your-own-prompts.html
│   └── ai-is-not-a-coding-tool.html
├── 404.html                    Served by GitHub Pages for missing paths (noindex)
├── robots.txt                  Crawl directives and sitemap location
├── sitemap.xml                 Indexable page and essay URLs
├── assets/
│   ├── site.css                Single stylesheet (light and dark mode, WCAG AA+ contrast)
│   └── og.png                  Open Graph preview image, 1200 × 630
├── favicon.svg                 "UT" monogram
├── scripts/check_links.py      Offline check that every internal link, fragment, OG URL, and sitemap entry resolves
├── .htmlvalidate.json          html-validate configuration
├── .github/workflows/checks.yml  CI: HTML validation and offline link check
├── docs/WHY.md                 Design choices and verification notes
├── .nojekyll                   Disables Jekyll processing on GitHub Pages
└── LICENSE                     MIT licence for code
```

## Preview locally

From the repository root:

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

Using a local HTTP server ensures folder URLs such as `writing/` and root-relative links in `404.html` and `<link rel="alternate" ... href="/writing/feed.xml">` resolve identically to GitHub Pages. Open <http://localhost:8000/404.html> directly to inspect the 404 page.

## Checks

```sh
npx --yes html-validate@11.16.1 index.html projects.html 404.html writing/*.html
python3 scripts/check_links.py
```

The first validates every HTML page against `html-validate`'s recommended rules (including structured JSON-LD metadata and SVG accessibility). The second reads every page and `sitemap.xml` from disk to confirm every internal link, `#fragment`, same-site Open Graph URL, and sitemap entry points at an existing file without making network requests.

## Adding an essay

1. Copy an existing page in `writing/` and update the title, meta description, canonical URL, Open Graph tags, byline, and body.
2. Keep the "Sources" section and closing "Related project" callout.
3. Add the essay to `writing/index.html`, `writing/feed.xml`, `sitemap.xml`, and (when featured) `index.html`.
4. Run `html-validate` and `scripts/check_links.py`.

## Publishing

This is a GitHub Pages user site deployed from the `main` branch root at `https://dsugurtuna.github.io`.

## Licence

- **Code** (HTML structure, CSS, and scripts): MIT. See [LICENSE](LICENSE).
- **Content** (essays and portfolio text): © 2026 Ugur Tuna. All rights reserved.

References to public guidance in the essays and reference kits are personal interpretations: unofficial and not government guidance.

---

<sub>Personal portfolio and open-source reference work. Views are my own.</sub>
