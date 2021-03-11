"""Sphinx configuration."""

project = "gentimer"
author = "teamikl"
copyright = f"2021, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    # "recommonmark",
    "m2r2",
]
html_theme = 'sphinx_rtd_theme'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md' : 'markdown',
}

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
