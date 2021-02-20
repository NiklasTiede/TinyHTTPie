import argparse
import requests
import collections
import sys


def main(argv=None):

    # give test suite access to CLI
    if not argv:
        argv = sys.argv[1:]

    parser = build_parser()
    args = parser.parse_args(argv)

    url = ""

    if args.URL:
        url = args.URL

    if ("http://" or "https://" or "http://www." or "https://www.") not in url:
        if url[:4] == "www.":
            url = url[4:]
        url = "http://" + url

    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Response Failed.")
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
        prog="tihttp",
        description=f"A tiny HTTP client for sending GET and POST requests.",
    )

    # positional arguments:
    parser.add_argument(
        "URL",
        action="store",
    )

    # optional arguments:
    parser.add_argument(
        "-H",
        "--header-only",
        dest="header",
        action="store_true",
        help="Prints only the header of the Response.",
    )

    parser.add_argument(
        "-B",
        "--body-only",
        dest="body",
        action="store_true",
        help="Prints only the body of the Response.",
    )
    return parser


def run_main():
    try:
        sys.exit(main())  # sys.argv
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(1)


if __name__ == "__main__":
    run_main()
