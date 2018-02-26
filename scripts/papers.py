import re, json
from pprint import pprint
from scripts.types import *


def smart_title(s):
    return ' '.join(w if w.isupper() else w.capitalize() for w in s.split())


re_papers = re.compile('<b>.*?.*?<a href="(.*?)">(.*?)<\/a>.*?href="(.*?)".*?<br.*?>(.*?)<br.*?>.*?<i>(.*?)<\/i>.*?<br.*?>(.*?)<br', flags=re.DOTALL | re.U)
re_bib = re.compile('@(\w+)\s*\{(.*?),')
re_bibitem = re.compile('(\w+).*?["\{](.*?)["\}]')

data = []
with open("publications.shtml", 'r') as f:
    s = ''.join(f.readlines())

matches = re_papers.findall(s)
for g in matches:
    p = build_papers(g)
    if p['bib'].find('bib.txt') >= 0:
        with open('../papers/BibTex/' + p['bib'], 'r') as f:
            s = f.readline()
            h = re_bib.match(s).groups()
            p['type'] = h[0].lower()
            p['bibname'] = h[1]
            lines = f.readlines()
            for line in lines:
                k = re_bibitem.match(line)
                print(line)
                if k is not None:
                    gg = k.groups()
                    bt = gg[0]
                    if bt == 'journal':
                        bt = 'booktitle'
                    if bt == 'event':
                        bt = 'series'
                    if bt == 'conference':
                        bt = 'location'
                    if p[bt] is None:
                        print(bt)
                    p[bt] = gg[1].strip()
        p['bib'] = p['bib'].replace('.bib.txt', '')
    data.append(p)

# pprint(data)

with open("../data/papers.json", 'w') as f:
    f.write(json.dumps(data, indent=4, sort_keys=False))
