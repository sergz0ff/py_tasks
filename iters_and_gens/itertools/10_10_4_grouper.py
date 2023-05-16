from itertools import zip_longest, repeat

def grouper(iterable, n):
    it = iter(iterable)
    return zip_longest(*[it for _ in range(n)])

numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))