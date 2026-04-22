# Repository Guidelines

## Project Structure & Module Organization

This repository contains Sphinx documentation for "Archie Docs". The active documentation sources are currently at the repository root:

- `conf.py` configures Sphinx, MyST, theme settings, and extensions.
- `index.md` is the main documentation entry point and toctree.
- `issue_fixes/` contains topic pages, such as troubleshooting and fix notes.
- `requirements.txt` lists Python documentation build dependencies.
- `.github/workflows/` contains GitHub Pages preview and deployment workflows.

If the source files are moved into a `docs/` directory, update `conf.py`, workflow paths, and build commands together.

## Build, Test, and Development Commands

Use Python 3.12 when possible to match CI.

- `python -m venv .venv` creates a local virtual environment.
- `source .venv/bin/activate` activates it on Linux/macOS shells.
- `python -m pip install -r requirements.txt` installs Sphinx and theme dependencies.
- `sphinx-build -b html . _build/html` builds the site from the current root layout.
- `python -m http.server 8000 -d _build/html` serves the generated HTML locally.
- `pre-commit run --all-files` runs formatting and hygiene checks.

## Coding Style & Naming Conventions

Write documentation in Markdown/MyST unless a page specifically needs reStructuredText. Use short, descriptive file names in lowercase with underscores, for example `issue_fixes/hyprland_kde_mime_fix.md`. Keep headings sentence-style and concise. Prefer fenced code blocks with language hints where applicable.

Formatting is managed by pre-commit hooks: `mdformat` for Markdown, `black` for Python files, `rstcheck` for reStructuredText, and `codespell` for spelling checks.

## Testing Guidelines

There is no application test suite. Treat documentation builds as the primary validation step. Before opening a pull request, run:

```sh
sphinx-build -b html . _build/html
pre-commit run --all-files
```

For new pages, add them to the `index.md` toctree so Sphinx includes them in navigation and link checking.

## Commit & Pull Request Guidelines

This repository currently has no local commit history, so no project-specific commit convention is established. Use concise imperative commit messages, such as `Add Hyprland MIME fix note` or `Update Sphinx Pages workflow`.

Pull requests should include a short summary, any related issue or context, and confirmation that the Sphinx build and pre-commit checks pass. Include screenshots only when visual theme, layout, or rendered content changes are significant.

## Agent-Specific Instructions

Keep generated changes focused on documentation and build configuration. Do not rewrite unrelated pages while adding a new topic. Preserve existing MyST/Sphinx conventions and verify that workflow paths match the actual source layout.
