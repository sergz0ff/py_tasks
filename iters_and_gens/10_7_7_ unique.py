def unique(iterable):
    res = {}
    for num in iterable:
        if num not in res:
            res[num] = num
    return iter(res)

numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))