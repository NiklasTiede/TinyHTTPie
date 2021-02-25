## 1. A Simple Script

This repository contains the code belonging to the first section of the article "[The Evolution of a Script](https://the-coding-lab.com/posts/the-evolution-of-a-script/)".

```python
import requests
import collections

resp = requests.get('https://the-coding-lab.com/')

header = dict(collections.OrderedDict(resp.headers))
body = resp.text

for section in sorted(header.items()):
    print(f"{section[0]}: {section[1]}")
```

<div>
<p align="center"> <a href="https://github.com/NiklasTiede/tinyHTTPie/tree/2-Sys-Module">section 2 >></a> </p>
</div>
