# 4. Distribution via Installation Script

This repository contains the code belonging to the fourth section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Here we created a shell script called `install.sh` to make things easier for the installation of tinyHTTPie.

```bash
git clone https://github.com/NiklasTiede/tinyHTTPie
cd tinyHTTPie
git checkout 4-Distributing-by-Installscript
./install.sh
```

It will create the directory `MyScripts` in your home directory, copy `tinyhttp.py`, and `requirements.txt` into it and rebuild the virtual environment using `pipenv`. The shebang line is added to the top of `tinyhttp.py`, the alias to your `.bashrc`/`.zshrc` or `.aliases` file.

```bash
tihttp -H google.com
```

voilà, the tool was installed using a shell script! But such a script can be quite error prone for someone like me and there's a nicer tool for installing python apps/libraries: the `setup.py` file!

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/3-Argparse-Module"><< section 3</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/5-Distributing-by-Setup-File">section 5 >></a> </p>
</div>
