# 7. Documentation

This repository contains the code belonging to the second section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Documentation can be supplied in different formats. Command line tools have a usage help (`--help`). For smaller projects the `README.md` can be sufficient enough whereas projects like libraries benefit from a more extensive hosted technical documentation (see [readthedocs](https://readthedocs.org/)).

Let's create some documentation!

```bash
pip install sphinx

mkdir docs
cd docs

sphinx-quickstart
```

Read the Docs prefers the reStructuredText format `.rst` for technical documentation instead of markdown.

filling questsions

```bash
cd ..
make html
```

if you open the index.html with you see its looks pretty puristic. Thats why I liek to use the rtd_theme:

```
pip install sphinx_rtd_theme
```

changing a little bit the `conf.py` file:

```python


```

Now again creating it:

```bash
make html
```

And it looks way nicer! OK next we wanna write some content to our documentation. We use the .srt syntax. (here's a nice cheatsheet)

Lets go into the `index.rst` file. I would advise to use a rst previewer to speed up things.
now lets do some changes

```bash

```

create html

And lastly we wanna publish it:

```bash

```

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/6-Testing-and-CI"><< section 6</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/8-Publishing-at-PyPI">section 8 >></a> </p>
</div>
