def with_previous(iterable):
    prev_tmp = None
    for i in iterable:
        yield (i, prev_tmp)
        prev_tmp = i

numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))