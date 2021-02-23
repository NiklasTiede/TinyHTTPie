# 7. Documentation

This repository contains the code belonging to the seventh section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Documentation can be supplied in different formats. Command line tools have a usage help (`--help`). For smaller projects the `README.md` can be sufficient enough whereas projects like libraries benefit from a more extensive hosted technical documentation (see [readthedocs](https://readthedocs.org/)).

Let's create some documentation! `sphinx` is a tool that will help us to create the documentation easily.

```bash
$ pip install sphinx

$ mkdir docs
$ cd docs
```

Sphinx will ask a couple of questions to fill out the

```
$ sphinx-quickstart

> Separate source and build directories (y/n) [n]: y
> Project name: tinyHTTPie
> Author name(s): Niklas Tiede
> Project release []: 0.1.0
> Project language [en]: enter
```

To create the documentation we have to use the `make html` command within the `docs` directory. This creates the HTML files of it.

```
$ cd ..
$ make html
```

If we open the `index.html` file in the browser we can see how our documentation will look like. But its appearance is pretty puristic. Therefore we use an often used theme to let it look nicer.

```
$ pip install sphinx_rtd_theme
```

Now we have to customize the `conf.py` file. We add the following lines:

```python
import sphinx_rtd_theme

extensions = ["sphinx_rtd_theme",]
pygments_style = "sphinx"
version = '0.1.0'
html_theme = 'sphinx_rtd_theme'
```

And render again.

```
$ make html
```

Now it looks way better! Ok, next we wanna write some more content. readthedocs should written in the reStructuredText syntax. Here's a nice [cheat sheet](https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst). A previewer will speed up things. I've added some documentation about tinyHTTPie, see [index.rst](https://github.com/NiklasTiede/tinyHTTPie/blob/7-Documentation/docs/source/index.rst), [install.rst](https://github.com/NiklasTiede/tinyHTTPie/blob/7-Documentation/docs/source/install.rst) and [tutorial.rst](https://github.com/NiklasTiede/tinyHTTPie/blob/7-Documentation/docs/source/tutorial.rst). The last step is to publish our documentation. We have to register at [readthedocs.org](https://readthedocs.org/) and connect it to our repository.

Voilà! We created our [tinyHTTPie documentation](https://tinyhttpie.readthedocs.io/en/latest/)! I hope you see how easy it is to setup a good-looking documentation. :smiley:

<div>
    <p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/6-Testing-and-CI"><< section 6</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/8-Publishing-at-PyPI">section 8 >></a> </p>
</div>
