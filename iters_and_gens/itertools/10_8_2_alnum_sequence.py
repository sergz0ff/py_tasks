from string import ascii_uppercase
from itertools import cycle

def alnum_sequence():
    alphabet = cycle(enumerate(list(ascii_uppercase), start=1))
    for pair in alphabet:
        yield from pair

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(99)))