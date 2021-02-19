# 3. Argparse Module

This repository contains the code belonging to the second section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

Here we took advantage of Python's sys module. This gives us the power to pass arguments from outside the script.

```python
#!/usr/bin/env python

import argparse
import requests
import collections
import sys


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv[1:])

    # print(vars(args))
    # print()

    url = ''

    if args.URL:
        url = args.URL

    if ('http://' or 'https://' or 'http://www.' or 'https://www.') not in url:
        if url[:4] == 'www.':
            url = url[4:]
        url = 'http://' + url

    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'Response Failed.')
        return 1

    header = dict(collections.OrderedDict(resp.headers))
    body = resp.text

    if args.body and not args.header:
        print(body)
        return 0

    if args.header and not args.body:
        for section in sorted(header.items()):
            print(f"{section[0]}: {section[1]}")
        return 0

    if (args.header and args.body) or (not args.header and not args.body):
        for section in sorted(header.items()):
            print(f"{section[0]}: {section[1]}")
        print()
        print(body)
        return 0

    return 1


def build_parser():
    parser = argparse.ArgumentParser(
        prog='tihttp',
        description=f'A tiny HTTP client for sending GET requests.'
    )

    # positional arguments:
    parser.add_argument(
    'URL',
    action='store',
    )

    # optional arguments:
    parser.add_argument(
    '-H',
    '--header-only',
    dest='header',
    action='store_true',
    help='Prints only the header of the Response.')

    parser.add_argument(
    '-B',
    '--body-only',
    dest='body',
    action='store_true',
    help='Prints only the body of the Response.')
    return parser


def run_main():
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(1)


if __name__ == '__main__':
    run_main()
```

<div>
<p align="center"><a href="https://github.com/NiklasTiede/tinyHTTPie/tree/2-Sys-Module"><< section 2</a> | <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/4-Distributing-by-Installscript">section 4 >></a> </p>
</div>
