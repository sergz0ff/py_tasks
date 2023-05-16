from itertools import chain, tee

def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))

print(*ncycles([1, 2, 3, 4], 3))