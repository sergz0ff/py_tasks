from sys import stdin
from re import fullmatch

# data = [line.strip() for line in stdin]
data = ['1 877 2638277', '91-011-23413627']

pat = r'(?P<Код_страны>\d{1,3})([- ]?)(?P<Код_города>\d{1,3})\2(?P<Номер>\d{4,10})'

for number in data:
    match = fullmatch(pat, number)
    content = match.groupdict() 
    for k, v in content.items():
        print(f'{k}: {v}')
    print()