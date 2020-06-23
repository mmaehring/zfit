#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020 zfit
#
# zfit documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.

import os
import sys
from pathlib import Path

import zfit

project_dir = Path(__file__).parents[1]
sys.path.insert(0, str(project_dir))

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '3.0.0'


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.githubpages',
              'sphinx.ext.napoleon',
              'sphinx_autodoc_typehints',  # must be imported after napoleon to properly work.
              # See https://github.com/agronholm/sphinx-autodoc-typehints/issues/15
              'sphinx.ext.todo',
              ]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'zfit'
copyright = zfit.__copyright__
author = zfit.__author__

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = zfit.__version__.split(('+'))[0]
# The full version, including alpha/beta/rc tags.
release = zfit.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Automatically add substitutions to all RST files.
with open('subst_types.txt') as subst_types:
    rst_epilog = subst_types.read()


# -- Napoleon settings ---------------------------------------------

using_numpy_style = False  # False -> google style
napoleon_google_docstring = not using_numpy_style
napoleon_numpy_docstring = using_numpy_style
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True


# -- sphinx_autodoc_typehints settings ---------------------------------------------

# if True, set typing.TYPE_CHECKING to True to enable “expensive” typing imports
set_type_checking_flag = False
# if True, class names are always fully qualified (e.g. module.for.Class). If False, just the class
# name displays (e.g. Class)
typehints_fully_qualified = False
# (default: False): If False, do not add ktype info for undocumented parameters. If True, add stub documentation for
# undocumented parameters to be able to add type info.
always_document_param_types = True
# (default: True): If False, never add an :rtype: directive. If True, add the :rtype: directive if no existing :rtype:
# is found.
typehints_document_rtype = True


# -- autodoc settings ---------------------------------------------

# also doc __init__ docstrings
autoclass_content = 'both'


# -- sphinx.ext.todo settings ---------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_logo = "images/zfit-fin_400x168.png"

html_theme_options = {
    "github_url": "https://github.com/zfit/zfit",
    "use_edit_page_button": True,
    "search_bar_text": "Search zfit..."
}

html_context = {
    "github_user": "zfit",
    "github_repo": "zfit",
    "github_version": "develop",
    "doc_path": "docs",
}

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'zfitdoc'

# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'zfit.tex',
     u'zfit Documentation',
     u'zfit', 'manual'),
]

# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'zfit',
     u'zfit Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'zfit',
     u'zfit Documentation',
     author,
     'zfit',
     'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

