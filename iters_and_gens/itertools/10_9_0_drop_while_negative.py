from itertools import dropwhile

def drop_while_negative(iterable):
    return (i for i in dropwhile(lambda x: x < 0, iterable))

numbers = [-3, -2, -1, 0, 1, 2, 3]

print(*drop_while_negative(numbers))

iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])

print(*drop_while_negative(iterator))