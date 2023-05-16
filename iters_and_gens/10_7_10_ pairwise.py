def pairwise(iterable):
    if iterable:
        iterable = iter(iterable)
        prev_tmp = next(iterable)
        for i in iterable:
            yield (prev_tmp, i)
            prev_tmp = i
        yield (prev_tmp, None)
    else:
        yield iterable

numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))