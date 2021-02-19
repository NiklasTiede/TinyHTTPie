## 2. Sys Module

This repository contains the code belonging to the second section of the article "The Evolution of a Script".

Here we took advantage of Python's `sys` module. This gives us the power to pass arguments from outside the script.

```python
#!/usr/bin/python

import requests
import collections
import sys

arg_array, input_url = sys.argv[1:], ''
body_bool, header_bool = False, False

if '-b' in arg_array:
    arg_array.remove('-b')
    body_bool = True

if '-h' in arg_array:
    arg_array.remove('-h')
    header_bool = True

if len(arg_array) > 1:
    print('Too many arguments')
    sys.exit(0)

if len(arg_array) == 1:
    input_url = arg_array[0]

if not input_url:
    print('No URL was given')
    sys.exit(0)

if 'http://www.' and 'https://www.' not in input_url:
    if input_url[:4] == 'www.':
        input_url = input_url[4:]
    input_url = 'http://www.' + input_url

try:
    r = requests.get(input_url)
except requests.exceptions.RequestException as e:
    print(f'Response Failed.')
header = dict(collections.OrderedDict(resp.headers))
body = resp.text

if body_bool and not header_bool:
    print(body)

if header_bool and not body_bool:
    for section in sorted(header.items()):
        print(f"{section[0]}: {section[1]}")

if (body_bool and header_bool) or (not body_bool and not header_bool):
    for section in sorted(header.items()):
        print(f"{section[0]}: {section[1]}")
    print()
    print(body)
```

Now we can decide to print only the header of the GET request:

```bash
tihttp -h https://the-coding-lab.com/
```

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/1-A-Simple-Script"><< section 1</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/3-Argparse-Module">section 3 >></a> </p>
</div>
