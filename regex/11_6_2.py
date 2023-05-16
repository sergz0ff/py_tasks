from sys import stdin
from re import fullmatch, search, match

# data = [line.rstrip() for line in stdin]
data = ['gogo', 'hohoho', 'XaXaXaXa', 'Python', 'beebee', 'PyPy', 'portal']
pattern = r"([A-Za-z][A-Za-z]+)(\1)"

for line in data:
    m = fullmatch(pattern, line)
    if m:
        try:
            m.group(3)
        except IndexError:
            print(line)
    
