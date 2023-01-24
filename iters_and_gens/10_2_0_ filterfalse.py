def filterfalse(func, iterable):
    if func is None:
        func = bool
    return filter(lambda elem: not func(elem), iterable)

objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))