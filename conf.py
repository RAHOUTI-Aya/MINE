# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GeneCure'
copyright = '2025, GIIA'
author = 'GIIA'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',  # Ajoute l'extension pour intégrer les notebooks Jupyter
    'sphinx.ext.mathjax',  # Permet d'afficher les mathématiques en LaTeX
    'sphinx.ext.githubpages',  # Permet la publication sur GitHub Pages
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

nbsphinx_execute = 'never'  # Ne pas exécuter les notebooks (si vous souhaitez que les notebooks ne soient pas exécutés à chaque génération)
