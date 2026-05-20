# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Static personal website for **Anik Jiménez Marulanda**, a Colombian writer. Five pages in Spanish, no build tools, no dependencies, no backend — open any `.html` file directly in a browser or serve with a local static server.

```
index.html      # Home / hero
sobre.html      # About the author
libros.html     # Books
palabra.html    # Featured quote page
contacto.html   # Contact form (frontend-only, fires an alert on submit)
styles.css      # All styles for all pages
```

## Development

No build step. To preview locally:

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

## Architecture

**Shared structure** — every page duplicates the same `<nav>`, `<footer>`, and inline scroll script. There is no templating engine; edits to nav or footer must be applied to each file manually.

**Active nav link** — the `.active` class on `<nav-links> a` is set statically per page (e.g. `<a href="sobre.html" class="active">`). It is not driven by JavaScript.

**Single stylesheet** — `styles.css` contains all layout, component, and page-specific styles in one file. Page sections are separated by comments (e.g. `/* ---------- Libros ---------- */`). The only exception is `palabra.html`, which has a small inline `<style>` block to override the background and nav color for its sage-gradient theme.

**No images** — the author photo is a CSS placeholder (`.photo-placeholder`). Book covers are pure CSS gradients and filters (`.cover-1`, `.cover-2`). No `<img>` tags exist yet.

**Typography** — two Google Fonts loaded from CDN: `Cormorant Garamond` (serif, for headings, quotes, and display text) and `Karla` (sans-serif, for body and UI). CSS custom properties for the color palette are defined in `:root` at the top of `styles.css`.

**Watercolor hero effect** — built entirely with CSS: multiple `.bloom` divs using `radial-gradient` + `filter: blur`, a `.grain` div using an inline SVG `feTurbulence` noise filter, and `mix-blend-mode: multiply`.

## Known issues

- `index.html:21` has a malformed closing tag: `Contacto<>/a>` — should be `Contacto</a>`.
