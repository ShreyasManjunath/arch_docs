# -- Project information -----------------------------------------------------
from pathlib import Path

project = "Archie Docs"
author = "Shreyas Manjunath"
release = "2026.04"
html_title = "Archie Docs"

# -- General config ----------------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    ".git",
    ".github",
    ".venv",
    "AGENTS.md",
    "README.md",
]

# -- HTML theme --------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"] if Path("_static").is_dir() else []

# Copybutton: ignore prompts in code blocks
copybutton_prompt_text = r">>> |\$ |ros2 "
copybutton_prompt_is_regexp = True

# Optional: If you later add a logo:
# html_logo = "_static/logo.png"
