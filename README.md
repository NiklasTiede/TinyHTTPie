# 6. Testing and CI

This repository contains the code belonging to the sixth section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Projects like these are too small to benefit from testing. But it's the goal of this tutorial to show the full tool set when creating a python package. We're using `pytest` the most popular testing tool within the Python community. We create a `tests` folder at the root level and add `__init__.py` and `test_tihttp.py` to it.

```python
├── LICENSE
├── README.md
├── setup.py
├── src
├── tihttp.py
├── tests
│  ├── __init__.py
│  ├── jsonplaceholder.json
│  └── test_tihttp.py
```

Then we write a test comparing the output of a GET request.

```python
from tihttp import main

def test_GET_body(capsys):
    main(["-B", "http://jsonplaceholder.typicode.com/todos?userId=1"])
    captured = capsys.readouterr()
    result = captured.out
    with open("tests/jsonplaceholder.json", "r") as f:
        output = f.read()
    assert result == output
```

Running pytest should be successful.

```bash
pytest
```

Thereafter we add pytest to out extra requirements in the `setup.py` file.

```python
extras_require={
    'dev': [
        'pytest', # pip install tihttp[dev]
    ],
},
```

This gives us the possibility to install extra dependencies (testing, linting tools etc.) easily by adding a `[dev]` to the package name.

```bash
pip install .[dev]
pip install tihttp[dev]
```

We tested all of this with python 3.7.3. But how does our application behave when executed on a different interpreter version? So let's test it against different Python versions! We use `tox`. It lets us run tests in multiple virtualenvs.

```bash
pip install tox
```

Tox needs a recipe to know which virtualenv/commands to create/execute. This recipe the `tox.ini` file.

```ini
[tox]
envlist = py36,py37,py38,py39

[testenv]
deps =
    pytest
commands =
    pytest
```

If some of the Python interpreters are missing on your system, install them from the deadsnakes archive:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.5 python3.6 python3.7 python3.8 python3.9
```

Now let's test across different interpreters!

```bash
tox
```

If you wanna test against a specific environment or execute only one test, then type:

```bash
tox -e py38
tox -e py38 -- test/main_test.py   # executes only single test
```

Ok we did the test locally, but when working in a team using continuous integration is pretty convenient. We set a `integrate.yaml` file up to tell github actions what jobs to do. 

```yaml
name: Python package

on: [push]

jobs:
  run:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8, 3.9]
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: Cache pip
        uses: actions/cache@v2
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
            ${{ runner.os }}-
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest pytest-cov
          pip install -r requirements.txt
      - name: Lint with flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
      - name: Test with pytest
        run: |
          pytest
```

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/5-Distributing-by-Setup-File"><< section 5</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/7-Documentation">section 7 >></a> </p>
</div>
