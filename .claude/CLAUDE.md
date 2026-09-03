# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Static personal website for **Anik Jiménez Marulanda**, a Colombian writer. Five pages in Spanish, no build tools, no dependencies, no backend — open any `.html` file directly in a browser or serve with a local static server.

```
index.html      # Home / hero
sobre.html      # Biography, values, mission, vision
libros.html     # Books
palabra.html    # Featured quote page
contacto.html   # Contact details + mailto form
styles.css      # All styles for all pages
images/         # Author photos and book cover
```

## Development

No build step. To preview locally:

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

## Architecture

**Shared structure** — every page duplicates the same `<nav>`, `<footer>`, and inline scroll script. There is no templating engine; edits to nav or footer must be applied to each file manually.

**Active nav link** — the `.active` class on `.nav-links a` is set statically per page. It is not driven by JavaScript.

**Single stylesheet** — `styles/styles.css` contains all layout, component, and page-specific styles.

**Brand direction** — beige/sand backgrounds, teal geometric triangle motifs, Great Vibes for the signature brandmark, Source Serif 4 for display/body, Outfit for UI labels. Content and visual language come from the author's creative portfolio.

**Imagery** — author portraits and book cover live under `images/`.
