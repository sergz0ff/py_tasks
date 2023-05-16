from itertools import chain, starmap
from functools import reduce

def sum_of_digits(iterable):
    res = 0
    return reduce(
        lambda x, y: x + y,
        starmap(lambda x: int(x), chain.from_iterable(''.join(str(e) for e in iterable)))
    )

print(sum_of_digits([13, 20, 41, 2, 2, 5]))
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))