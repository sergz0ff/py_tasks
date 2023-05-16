from itertools import pairwise

def is_rising(iterable):
    return all(
        map(
        lambda x: x[0] < x[1],
        pairwise(iterable)
        )
    )

print(is_rising([1, 2, 3, 4, 5]))

iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))