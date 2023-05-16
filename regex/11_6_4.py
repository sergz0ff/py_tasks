from sys import stdin
from re import search, fullmatch, match

# data = [line.rstrip() for line in stdin]
data = [
    'hi, beegeek', 
    'beegeek is an awesome place for programmers',
    'beegeek rocks, rocks beegeek',
    'i think beegeek is a great place to hangout'
    ]

pattern1 = r"^beegeek.*beegeek$"
pattern2 = r"^beegeek.+[^beegeek]$|^[^beegeek].+beegeek$"
pattern3 = r"beegeek"

patterns = [(3, pattern1), (2, pattern2), (1, pattern3)]
counter = 0

for line in data:
    for score, pattern in patterns:
        if search(pattern, line):
            counter += score
            break
            
print(counter)