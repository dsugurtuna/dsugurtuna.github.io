# Why it's built this way

A personal site has two jobs: say clearly who I am and what I work on, and point to evidence someone can check. It should be fast, readable for everyone and cheap to keep correct, so the effort goes into the content rather than the machinery.

## Design choices

**Why plain HTML with no build step?** Because the site is a handful of pages that change rarely. A static site generator would add a toolchain to keep up to date and a place for things to break between writing and publishing. GitHub Pages serves static files anyway, so the files in the repository are exactly what readers get.

**Why no JavaScript?** Because nothing on the site needs it. Light and dark mode follow the operating system through CSS, and navigation is ordinary links. No script means nothing to load, nothing to break and nothing to audit.

**Why no analytics or trackers?** Because readers should not have to be tracked to read a few essays. It also fits the first essay: a visit count would say who clicked, not whether the writing was any good.

**Why system fonts instead of web fonts?** Because web fonts cost an extra request, can tell a third party who is reading, and can make text jump as they load. The serif stack asks for faces that already ship with each platform (Iowan Old Style or Charter on Apple devices, Sitka or Cambria on Windows) and falls back to the platform's default serif elsewhere.

**Why one stylesheet built on custom properties?** Because light and dark mode then share every rule and only the colour tokens change. One accent colour keeps the look calm and makes links easy to spot. Every text colour pair meets WCAG AA contrast in both schemes, and axe-core reports no contrast violations.

**Why does `404.html` use root-relative links when every other page uses relative ones?** Because GitHub Pages serves `404.html` at whatever missing path was requested, such as `/writing/old/page`. Relative links would then resolve against the wrong folder. Everywhere else, relative links keep the site working in any local preview.

**Why a small Python link checker rather than a crawler?** Because the site is a few files on disk. Reading them directly is fast, needs no server or dependencies, works offline and behaves the same locally and in CI. It checks fragments (`#main`) and same-site Open Graph URLs as well as ordinary links.

**Why pin the html-validate version in CI?** Because a new release can add rules. A pinned version means a failing check points to a change in this repository, not a change in the tool.

## Questions worth asking

**Without analytics, how will you know the site works?** By checking the things that can be checked: every page validates, every internal link resolves and the accessibility checks pass, on every change. Whether the writing is useful is a judgement for readers, and they can say so through GitHub or my website. If I ever need numbers, I would want something that counts pages without identifying people, and I would say so on the site.

**Why should anyone trust essays drafted with AI assistance?** They should trust them only as far as they can check them. Each essay cites its public sources with links, makes no statistical claims, and is limited to what those sources actually say. Guidance is described as my reading of it: unofficial, and not government guidance. The drafts are a starting point. I read and rewrite them before they go out, and I own what is published.

**Does it hold up for keyboard and screen-reader users?** It has a skip link, one `main` landmark per page, a labelled navigation with the current page marked, visible focus outlines and headings in order. axe-core finds no violations on any page in either colour scheme at desktop and phone widths. What remains unverified: I have not yet tested it with a screen reader such as VoiceOver or NVDA, and automated tools do not catch everything.

## What comes next

- Run the axe-core check in CI, not only locally.
- Test with VoiceOver and NVDA and fix what they find.
- Add an Atom feed once there are enough essays to make one worthwhile.
