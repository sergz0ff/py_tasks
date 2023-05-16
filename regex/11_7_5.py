from sys import stdin
from bs4 import BeautifulSoup as bs
from collections import defaultdict

res = defaultdict(set)
for line in stdin:
    for tag in bs(line, 'html.parser')():
        res[tag.name] = set(tag.attrs)

for k, v in sorted(res.items()):
    print(f'{k}: ', end='')
    print(*sorted(v))
    
