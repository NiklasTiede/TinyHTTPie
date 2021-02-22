# 6. Testing and CI

This repository contains the code belonging to the sixth section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Projects like these are too small to benefit from testing. But it's the goal of this tutorial to show the full tool set when creating a python package. We're using `pytest` the most popular testing tool within the Python community. We create a `tests` folder at the root level and add `__init__.py` files to the `tests` and the `src` folder (So that pytest finds everything).

```python
├── LICENSE
├── README.md
├── setup.py
├── src
│  └── tihttp
│     ├── __init__.py
│     └── main.py
├── tests
│  ├── __init__.py
│  ├── jsonplaceholder.json
│  └── test_main.py
```

To be able to import the argument parser
we have to modify our `main.py` file. Now we can import the main-function and add arguments as list from within out `test_main.py` file to test our application.

```python
def main(argv=None):

    if not argv:
        argv = sys.argv[1:]

...

def run_main():
    try:
        sys.exit(main())  # sys.argv
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(1)
```

For this test we compare the body of the response of a GET request with the expected response.

```python
from src.tihttp.main import main

def test_GET_body(capsys):
    main(["-B", "http://jsonplaceholder.typicode.com/todos?userId=1"])
    captured = capsys.readouterr()
    result = captured.out
    with open("tests/jsonplaceholder.json", "r") as f:
        output = f.read()
    assert result == output
```

To test we just type `pytest`. The test was successful.

```bash
pytest
```

We add pytest to out extra reqiurements in the setup.py file.

```python
extras_require={
    'dev': [
        'pytest', # pip install tihttp[dev]
    ],
},
```

This will give us the possibility to install the extra dependencies for developers of the project easily by adding a [dev].

```bash
pip install .[dev]
pip install tihttp[dev]
```

We tested this all with python 3.7.3. But how does our application behave when executed on a different interpreter version? Just test it against different python versions! We use `tox`.

running tests in multiple virtualenvs

```bash
pip install tox
```

Then creating a `tox.ini` file.

```ini
[tox]
envlist = py35,py36,py37,py38,py39

[testenv]
# install pytest in the virtualenv where commands will be executed
deps = pytest
commands =
    # NOTE: you can run any command line tool here - not just tests
    pytest
```

using tox will do the jobs. it creates venvs and executes the commands of the tox.ini file

If you havent the python interpreters install them

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.5 python3.6 python3.7 python3.8 python3.9
```

this executes everything

```bash
tox
tox -e py38   # if you wanna test only version 3.8 and skip others
```

toxtest
Travis CI, Github Actions,
codecov

CI: github actions

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/5-Distributing-by-Setup-File"><< section 5</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/7-Documentation">section 7 >></a> </p>
</div>
