def pairwise(iterable):
    iterable = iter(iterable)
    prev_tmp = next(iterable)
    for i in iterable:
        yield (prev_tmp, i)
        prev_tmp = i
    yield (prev_tmp, None)

numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))