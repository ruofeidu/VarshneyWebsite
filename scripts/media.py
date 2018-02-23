import re, json
from pprint import pprint
from scripts.types import *

re_media = re.compile("\d+\.\s(.+),\s“(.+)”\s(\w+)\s(\d+),\s(\d+)(.*)\:.*(http.+)")
lines = []
data = []
with open("media.txt", 'r') as f:
    lines = f.readlines()
for line in lines:
    m = re_media.match(line)
    g = m.groups()
    data.append(build_media(g))

print(pprint(data))

with open("media.json", 'w') as f:
    f.write(json.dumps(data, indent=4, sort_keys=False))
