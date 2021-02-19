# 5. Distributing by Setup File

This repository contains the code belonging to the second section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Writing shell scripts for installation can be an entry point of vulnerabilities. The Python community created `setup.py` files for installation.

```python



```

with the help of this file we can easily install the script:

```bash
git clone https://github.com/NiklasTiede/tinyHTTPie/tree/5-Distributing-by-Setup-File.git
cd tinyHTTPie
pip install .
pip install setup.py
pip install
```

or by using the git-url directly. Direct installation from git can take much time especially for projects which are bigger and use non-Python languages. THerefore its preferabble to download everything from the PyPI or conda repo.

```bash
pip install git+https://github.com/NiklasTiede/tinyHTTPie/tree/5-Distributing-by-Setup-File.git
```

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/4-Distributing-by-Installscript"><< section 4</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/6-Testing-and-CI">section 6 >></a> </p>
</div>
