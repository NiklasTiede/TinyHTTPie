# 8. Publishing at PyPI

This repository contains the code belonging to the eighth section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Ok, now people can download our project from github and use it. But in our daily work we use the packaging python index. So how do we release our package on PyPI? First we have to decide which versioning scheme we will use. Semantic versioning ([semver.org](https://semver.org/)) and calendar versioning ([calver.org](https://calver.org/)) are commonly used. We decide to use semantic versioning in the following. Github allows us to make images of our project (tags). Often the tagging corresponds with the package releases on PyPI. So let's first create a tag:

```
$ git add .
$ git commit -m "v1.0.0"
$ git tag !$
```

Tags are a great opportunity to see a project in reverse at every stage of its development. Next we will generate a source distribution (.tar.gz) and a wheel distribution (.whl).

```
$ pip install wheel

$ python setup.py sdist bdist_wheel
```

The generated files can be found within the `dist` directory. Next we have to register at [PyPI](https://pypi.org/) before we can upload our project. For testing purposes it's convenient to upload the project to [TestPyPI](https://test.pypi.org/). So, let's do that first.

```
$ pip install twine

$ twine upload --repository testpypi dist/*
```

Now let's test installing `tihttp`.

```
$ pip install -i https://test.pypi.org/pypi/ --extra-index-url https://pypi.org/simple tihttp
```

Our tools works perfectly fine!

```
$ tihttp -H google.com
```

---

And now that we are sure that everything works, it's time to upload things to PyPI.

```
$ twine upload --repository pypi dist/*

$ pip install tihttp
```

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/7-Documentation"><< section 7</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/9-Publishing-at-Anaconda">section 9 >></a> </p>
</div>
