# 9. Publishing at Anaconda

This repository contains the code belonging to the ninth section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

When a `setup.py` file was already created, it's pretty simple to go a step further and make an [Anaconda](https://anaconda.org) package. The metadata of the `setup.py` file can be imported via jinja2 templating into the `meta.yml` file.

```yaml
{% set data = load_setup_py_data() %}

package:
  name: 'tihttp'
  version: {{ data['version'] }}

source:
  path: ..

build:
  number: 0
  entry_points:
    {% for entry_point in data['entry_points']['console_scripts'] %}
    - {{ entry_point }}
    {% endfor %}
  script: python -m pip install --no-deps --ignore-installed .

requirements:
  build:
    - python
    - pip
    - setuptools

  run:
    - python
    {% for dep in data['install_requires'] %}
    - {{ dep.lower() }}
    {% endfor %}

test:
  imports:
    - {{ data['name'] }}
  source_files:
    - tests
  requires:
    {% for test_dep in data['extras_require']['dev'] %}
    - {{ test_dep.lower() }}
    {% endfor %}
  commands:
    - pytest tests

about:
  home: {{ data['url'] }}
  license: {{ data['license'] }}
  summary: {{ data['description'] }}
  doc_source_url: {{ data['url'] + '/blob/master/README.md' }}
```

Now we can build the package.

```
$ conda build .
```

The generated file `tihttp-0.1.0-py37_0.tar.bz2` can be found within the `anaconda3/conda-build/linux-64` directory. To upload the package to the anaconda repository we have to register and then we can use the `anaconda upload` command.

```
$ anaconda upload home/niklas/anaconda3/conda-build/linux-64/tihttp-0.1.0-py37_0.tar.bz2

$ conda install -c niklastiede tihttp
```

But building and uploading packages for different Python interpreter versions and different operating systems is tedious. This work can be automated by a bash script:

```bash
#!/bin/bash

export PATH=~/anaconda3/bin:$PATH
pkg='tihttp'
array=( 3.6 3.7 3.8 3.9 )


# delete old built packages
if [[ -d $HOME/conda-bld/ ]]; then
    rm -r $HOME/conda-bld/
fi
for i in $HOME/anaconda3/conda-bld/linux-64/$pkg*; do
    echo $i
    rm $i
done
echo "Deleting old conda packages done!"


# building conda packages
for i in "${array[@]}"
do
    echo $i
	conda build --py $i .
done
echo "Building conda packages done!"


# converting conda packages to other platforms
platforms=( osx-64 linux-32 linux-64 win-32 win-64 )
for file in $HOME/anaconda3/conda-bld/linux-64/$pkg*; do
    echo $file
    conda convert --platform all $file  -o $HOME/conda-bld/
    for platform in "${platforms[@]}"
    do
        conda convert --platform $platform $file  -o $HOME/conda-bld/
    done
done
echo "converting packages to other platforms done!"


# uploading packages
find $HOME/conda-bld/**/$pkg*.tar.bz2 | while read file
do
    anaconda upload $file
done
echo "Uploading conda packages done!"
```

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/8-Publishing-at-PyPI"><< section 8</a></p>
</div>
