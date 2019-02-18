import re, json
from pprint import pprint
from scripts.types import *


def smart_title(s):
  return ' '.join(w if w.isupper() else w.capitalize() for w in s.split())


re_members = re.compile(
    'memberpic.*?href="(.*?)".*?src="(.*?)".*?href=.*?."\>(.*?)\<.*?\/div\>',
    flags=re.DOTALL | re.U)
data = []
with open("members.shtml", 'r') as f:
  s = ''.join(f.readlines())

matches = re_members.findall(s)
for g in matches:
  data.append(build_student(g))

pprint(data)

with open("../data/students.json", 'w') as f:
  f.write(json.dumps(data, indent=4, sort_keys=False))
