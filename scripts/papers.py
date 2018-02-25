import re, json
from pprint import pprint
from scripts.types import *


def smart_title(s):
    return ' '.join(w if w.isupper() else w.capitalize() for w in s.split())


re_papers = re.compile('<b>.*?<\/b>.*?<a href="(.*?)">(.*?)<\/a>.*?<br.*?>(.*?)<br.*?>.*?<i>(.*?)<\/i>.*?<br.*?>.*?<br', flags=re.DOTALL | re.U)
data = []
with open("publications.shtml", 'r') as f:
    s = ''.join(f.readlines())

matches = re_papers.findall(s)
for g in matches:
    data.append(build_papers(g))

pprint(data)

with open("../data/papers.json", 'w') as f:
    f.write(json.dumps(data, indent=4, sort_keys=False))
