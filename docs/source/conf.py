# Configuration file for the Sphinx documentation builder.

import datetime

# -- Project information

project = "IMAS Data Dictionary"
copyright = f"{datetime.datetime.now().year}, ITER Organization"
author = "ITER Organization"

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx_immaterial",
]

intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = ["_build"]

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = "sphinx_immaterial"
html_theme_options = {
    "repo_url": "https://git.iter.org/projects/IMAS/repos/data-dictionary",
    "repo_name": "Data Dictionary",
    "icon": {
        "repo": "fontawesome/brands/bitbucket",
    },
    "features": [
        # "navigation.expand",
        # "navigation.tabs",
        "navigation.sections",
        "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        # "search.share",
        # "toc.integrate",
        # "toc.follow",
        "toc.sticky",
        # "content.tabs.link",
        "announce.dismiss",
    ],
    # "toc_title_is_page_title": True,
    # "globaltoc_collapse": True,
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "light-green",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "light-blue",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    #"version_dropdown": True,
    #"version_json": "../versions.js",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

