#!/usr/bin/env python3
"""Check that every internal link on the site resolves.

Why a script and not a crawler? Because the site is a handful of static files:
reading them from disk is fast, needs no server and no dependencies, and runs
the same way locally and in CI.

What it checks, for every .html file in the repository:
- href and src attributes that point inside the site (relative, root-relative,
  or absolute URLs on https://dsugurtuna.github.io) resolve to a real file;
- fragment links (#id) point at an id that exists in the target page;
- Open Graph URLs (og:url, og:image) on the site's own domain resolve too.

External links are listed but not fetched, so the check works offline.

Usage: python scripts/check_links.py
"""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE_ORIGIN = "https://dsugurtuna.github.io"
SKIP_DIRS = {".git", "node_modules"}


class PageParser(HTMLParser):
    """Collect link targets and element ids from one HTML page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        if "id" in values:
            self.ids.add(values["id"])
        for attr in ("href", "src"):
            if attr in values:
                self.links.append(values[attr])
        if tag == "meta" and values.get("property") in {"og:url", "og:image"}:
            self.links.append(values.get("content", ""))


def html_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.html") if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts)
    )


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def resolve(page: Path, link: str) -> tuple[Path | None, str]:
    """Return (target file, fragment) for an internal link, or (None, '') if external."""
    if link.startswith(SITE_ORIGIN):
        link = link[len(SITE_ORIGIN):] or "/"
    parts = urlsplit(link)
    if parts.scheme or parts.netloc:
        return None, ""
    path = unquote(parts.path)
    if not path:
        target = page
    elif path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = page.parent / path
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target.resolve(), parts.fragment


def main() -> int:
    pages = {p.resolve(): parse(p) for p in html_files()}
    errors: list[str] = []
    internal = external = 0

    for page, parsed in pages.items():
        rel_page = page.relative_to(ROOT)
        for link in parsed.links:
            if link.startswith(("mailto:", "tel:")):
                continue
            target, fragment = resolve(page, link)
            if target is None:
                external += 1
                continue
            internal += 1
            if not target.is_file():
                errors.append(f"{rel_page}: '{link}' -> missing file")
                continue
            if fragment:
                ids = pages[target].ids if target in pages else set()
                if fragment not in ids:
                    errors.append(f"{rel_page}: '{link}' -> no element with id '{fragment}'")

    for error in errors:
        print(f"BROKEN  {error}")
    print(
        f"Checked {len(pages)} pages: {internal} internal links, "
        f"{len(errors)} broken; {external} external links not fetched."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
