from functools import lru_cache
import sys

@lru_cache
def alpha(string):
    string = ''.join(sorted(list(string)))
    return string

lines = sys.stdin.read().split()
for line in lines:
    print(alpha(line))