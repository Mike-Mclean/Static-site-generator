# Static Site Generator

A custom static site generator written in Python. It converts Markdown files in the `content/` directory into static HTML pages under `docs/` using an HTML template and copying assests from `static/`.

This project is based on the [Boot.dev](https://www.boot.dev/courses/build-static-site-generator-python).

## Features

- Converts Markdown (`.md`) to HTML using a custom parser
- Supports:
  - Headings (`#`, `##`, etc.)
  - Paragraphs (blank-line separated)
  - Code blocks (```) that preserve formatting
  - Blockquotes (`>`)
  - Unordered and ordered lists
  - Inline formatting: **bold**, _italic_, `inline code`
  - Links and images
- Uses an HTML template (`template.html`) for all pages
- Copies static assets from `static/` into the output directory
- Copies Directory structure of `content/` into `docs/`


## Getting Started

### Prerequisites

- Python 3.8+ (tested with Python 3.11)

### Run the generator

From the project root:

```bash
./main.sh
```

Or run directly:

```bash
python3 src/main.py
```

By default, generated site files are written to `docs/`.

### Base path (optional)

If you need the site to work under a URL base path, pass it as the first argument:

```bash
python3 src/main.py /URL-BASE-PATH/
```

This rewrites absolute `href="/…"` and `src="/…"` paths in the template so links work when hosted under a subpath.


## Project Structure

```
content/        # Markdown source pages
static/         # CSS, images, and other static assets
template.html   # HTML template used for every page
src/            # Static site generator implementation
docs/           # Generated site output (built by running main.sh)
```

### Content layout

Each folder in `content/` becomes a directory in the generated site.

- `content/index.md` → `docs/index.html`

> Note: The generator always writes `index.html` for each directory (it doesn’t preserve the original file name).


## Customizing the Template

The template must include the placeholders:

- `{{ Title }}` — replaced with the first Markdown heading (`#`) from the page
- `{{ Content }}` — replaced with the rendered HTML of the Markdown file
