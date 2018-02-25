import re, json
from pprint import pprint
from scripts.types import *


def smart_title(s):
    return ' '.join(w if w.isupper() else w.capitalize() for w in s.split())


re_media = re.compile("\d+\.\s(.+),\s“(.+)”\s(\w+)\s(\d+),\s(\d+)(.*)\:.*(http.+)")
lines = []
data = []
with open("media.txt", 'r') as f:
    lines = f.readlines()
for line in lines:
    m = re_media.match(line)
    g = m.groups()
    data.append(build_media(g))

pprint(data)

with open("media.json", 'w') as f:
    f.write(json.dumps(data, indent=4, sort_keys=False))
