from sys import stdin
from re import fullmatch

pattern = r"_\d+[A-Za-z]*_?"

for line in stdin:
    print(
        bool(
        fullmatch(pattern, line.rstrip())
        )
    )