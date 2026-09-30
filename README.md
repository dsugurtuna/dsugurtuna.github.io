# dsugurtuna.github.io

Source for my personal site: [dsugurtuna.github.io](https://dsugurtuna.github.io).

Plain HTML and one stylesheet. No build step, no framework, no JavaScript, no trackers, no web fonts and no CDNs. GitHub Pages serves the files exactly as they are in this repository.

> **Note on the essays.** The essays were drafted with AI assistance. Before publishing, read each one aloud and rewrite anything you would not say yourself.

## Structure

```text
.
├── index.html                  Home: headline, now/before/thread, flagship projects,
│                               how I work, track record, writing, contact
├── projects.html               Every repository, grouped as in the GitHub profile README
├── writing/
│   ├── index.html              List of essays
│   ├── usage-is-not-quality.html
│   ├── a-second-model-is-a-critic.html
│   └── read-freely-write-carefully.html
├── 404.html                    Served by GitHub Pages for any missing path
├── assets/
│   ├── site.css                The only stylesheet (light and dark mode)
│   └── og.png                  Open Graph preview image, 1200 × 630
├── favicon.svg                 "UT" monogram
├── scripts/check_links.py      Offline check that every internal link resolves
├── .htmlvalidate.json          html-validate configuration
├── .github/workflows/checks.yml  CI: HTML validation and link check
├── docs/WHY.md                 Why it's built this way
├── .nojekyll                   Tells GitHub Pages not to run Jekyll
└── LICENSE                     MIT, for the code
```

## Preview locally

From the repository root:

```sh
python -m http.server 8000
```

Then open <http://localhost:8000>.

Why a local server rather than opening the files directly? Folder links such as `writing/` and the root-relative links in `404.html` only resolve over HTTP. Python's server does not serve `404.html` for missing paths the way GitHub Pages does, so open <http://localhost:8000/404.html> to see it.

## Checks

```sh
npx --yes html-validate@11.16.1 index.html projects.html 404.html writing/*.html
python scripts/check_links.py
```

The first validates every page against html-validate's recommended rules. The second reads every page from disk and confirms that each internal link, fragment and same-site Open Graph URL points at something that exists. It needs only the Python standard library and does not fetch external links. CI runs both on every push to `main` and on pull requests.

Accessibility was checked with [axe-core](https://github.com/dequelabs/axe-core) (WCAG 2.2 A and AA rules plus best practice) on every page, in light and dark colour schemes, at 1280px and 390px wide. That check is not in CI yet.

## Adding an essay

1. Copy an existing page in `writing/` and change the title, meta description, canonical URL, Open Graph tags, byline and body.
2. Keep the "Sources" section and the closing "Related project" link.
3. Add the essay to `writing/index.html` and to the Writing section of `index.html`.
4. Run the checks above.

## Publishing

This is a GitHub Pages user site. In the repository settings, under Pages, deploy from the `main` branch and the root folder. The site then appears at `https://dsugurtuna.github.io`.

## Licence

- **Code** (HTML structure, CSS and scripts): MIT. See [LICENSE](LICENSE).
- **Content** (the essays and other writing on the site): © 2026 Ugur Tuna. All rights reserved.

References to public guidance in the essays are my own reading of it: unofficial; not government guidance.

---

<sub>Personal site. Views are my own. Not affiliated with or endorsed by any employer.</sub>
