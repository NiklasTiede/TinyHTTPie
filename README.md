# tinyHTTPie

This repository contains the code to the multi-part series "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Each branch contains the HTTP client `tinyhttp` at a different stage of its development.

<h1 id="contents" ><img src="docs/contents.png" width="30px"> Contents</h1>

1. [A Simple Script](https://github.com/NiklasTiede/tinyHTTPie/tree/1-Simple-Script)
2. [Sys Module](https://github.com/NiklasTiede/tinyHTTPie/tree/2-Sys-Module)
3. [Argparse Module](https://github.com/NiklasTiede/tinyHTTPie/tree/3-Argparse-Module)
4. [Distribution via install.sh](https://github.com/NiklasTiede/tinyHTTPie/tree/4-Distributing-by-Installscript)
5. [Distribution via setup.py](https://github.com/NiklasTiede/tinyHTTPie/tree/5-Distributing-by-Setup-File)
6. [Testing and CI](https://github.com/NiklasTiede/tinyHTTPie/tree/6-Testing-and-CI)
7. [Documentation](https://github.com/NiklasTiede/tinyHTTPie/tree/7-Documentation)
8. [Publishing at PyPI](https://github.com/NiklasTiede/tinyHTTPie/tree/8-Publishing-at-PyPI)
9. [Publishing at Anaconda](https://github.com/NiklasTiede/tinyHTTPie/tree/9-Publishing-at-Anaconda)

---

The version of tinHTTPie within this main branch is the most advanced version.

<h1 id="installation" ><img src="docs/installation.png" width="28px"#> Installation</h1>

Can be easily downloaded, built and installed via `pip`.

```
pip install git+https://github.com/NiklasTiede/tinyHTTPie
```

<h1 id="example" ><img src="docs/example.png" width="34px"#> Example</h1>

Some GET requests from the command line.

```console
❯ tihttp -H google.com
Cache-Control: private, max-age=0
Content-Encoding: gzip
Content-Length: 5649
Content-Type: text/html; charset=ISO-8859-1
Date: Sat, 20 Feb 2021 17:08:42 GMT
...

❯ tihttp -B http://jsonplaceholder.typicode.com/todos?id=1
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  }
]
```

I hope you could find something useful for yourself, I'm thankful for every pull request :smile:
