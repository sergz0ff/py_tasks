from sys import stdin
from re import fullmatch, search

# data = [line.rstrip() for line in stdin]
data = ['beebee bee', 'beegeek', 'bee geek bee']

pattern1 = r"(.*bee.*){2,}"
pattern2 = r"\bgeek\b"

res = {
    'pattern1': 0,
    'pattern2': 0
}

for row in data:
    if fullmatch(pattern1, row):
        res['pattern1'] += 1
    if search(pattern2, row):
        res['pattern2'] += 1

for v in res.values():
    print(v)