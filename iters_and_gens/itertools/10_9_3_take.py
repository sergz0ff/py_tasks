from itertools import islice

def take(iterable, n):
    return islice(iterable, 0, n)

print(*take(range(10), 5))