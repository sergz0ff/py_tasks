def flatten(nested_list):
    for i in nested_list:
        if type(i) is int:
            yield i
        if type(i) is list:
            yield from flatten(i)

generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)