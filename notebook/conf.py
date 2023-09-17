extensions = [
    "myst_nb",
    'sphinx_copybutton',             # sphinx-copybutton.readthedocs.io
    'sphinx_design',                 # github.com/executablebooks/sphinx-design
    'sphinx_togglebutton',           # sphinx-togglebutton.readthedocs.io
    "sphinx.ext.githubpages",
]

myst_enable_extensions = ['colon_fence', 'deflist', 'dollarmath', 'html_image', 'substitution']

master_doc = "index"
project = "聪明办法学 Python"
copyright = "2022 - 2023 Datawhale P2S Team"
author = "P2S Team"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
nitpicky = True

language = "zh_CN"
html_theme = "furo"
html_title = "<div align=center><small>聪明办法学 Python</small></div>"
html_logo = "./image/datawhale_logo.png"
html_theme_options = {
    "announcement": "聪明办法学 Python 在线文档 Beta 测试",
    "source_repository": "https://github.com/anine09/p2s-book",
    "source_branch": "main",
    "source_directory": "docs/",

}

nb_number_source_lines = True
nb_execution_mode = 'off'
execution_in_temp = True
