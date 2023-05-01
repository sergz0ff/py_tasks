def with_previous(iterable):
    prev_tmp = None
    for i in iterable:
        yield (prev_tmp)
        prev_tmp = i

def pairwise(iterable):
    if iterable:
        iterable = iter(iterable)
        prev_tmp = next(iterable)
        for i in iterable:
            yield (i)
            prev_tmp = i
        yield (None)
    else:
        yield iterable

def around(iterable):
    iterable = list(iterable)
    return zip(with_previous(iterable),iter(iterable),pairwise(iterable))

# numbers = [1, 2, 3, 4, 5]

# print(*around(numbers))

iterator = iter('hey')

print(*around(iterator))