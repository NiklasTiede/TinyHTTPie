import requests
import collections

resp = requests.get('https://the-coding-lab.com/')

header = dict(collections.OrderedDict(resp.headers))
body = resp.text

for section in sorted(header.items()):
    print(f"{section[0]}: {section[1]}")