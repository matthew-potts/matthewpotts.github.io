author = 'Matthew Potts'
bibtex_bibfiles = ['references.bib']
comments_config = {'hypothesis': False, 'utterances': False}
copyright = '2025'
exclude_patterns = ['**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '_build']
extensions = ['sphinx_togglebutton', 'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinx_thebe', 'sphinx_comments', 'sphinx_external_toc', 'sphinx.ext.intersphinx', 'sphinx_design', 'sphinx_book_theme', 'sphinxcontrib.bibtex', 'sphinx_jupyterbook_latex', 'sphinx_multitoc_numbering']
external_toc_exclude_missing = False
# external_toc_path = '_toc.yml'
html_baseurl = ''
html_context = {'default_mode': 'light'}
html_css_files = ['custom.css']
html_favicon = 'logo.png'
html_logo = 'logo.png'
html_sourcelink_suffix = ''
html_sidebars = {
  "**": [],
}
html_show_sourcelink = False
html_static_path = ['_static']
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': '', 'jupyterhub_url': '', 'thebe': False, 'colab_url': '', 'deepnote_url': ''}, 
    'path_to_docs': 'docs', 'repository_url': 'https://github.com/matthew-potts/matthew-potts.github.io', 'repository_branch': 'master', 'extra_footer': '', 'home_page_in_toc': True, 'announcement': '', 'analytics': {'google_analytics_id': '',
    'plausible_analytics_domain': '', 'plausible_analytics_url': 'https://plausible.io/js/script.js'}, 'use_repository_button': False, 'use_edit_page_button': False, 'use_issues_button': False,
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/matthew-potts/",
            "icon": "fa-brands fa-github"
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/matthew-potts-524aa224/",
            "icon": "fa-brands fa-linkedin"
        }
    ],
}
html_title = 'The Evolution of Cross-Border Funding - View from the BIS Data API and getBISy'
latex_engine = 'pdflatex'
myst_enable_extensions = ['colon_fence', 'dollarmath', 'linkify', 'substitution', 'tasklist']
myst_url_schemes = ['mailto', 'http', 'https']
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = 'off'
nb_execution_timeout = 30
nb_output_stderr = 'show'
numfig = True
pygments_style = 'sphinx'
suppress_warnings = ['myst.domains']
use_jupyterbook_latex = True
use_multitoc_numbering = True
