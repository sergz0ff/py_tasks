def get_min_max(iterable):
    if type(iterable) is list and iterable:
        return min(iterable), max(iterable)
    elif type(iterable) is list and not iterable:
        return None
    else:
        try:
            start = next(iterable)
            end = start
        except StopIteration:
            return None
        for i in iterable:
            if i > start:
                start = i
            if i < end:
                end = i
        return end, start


iterable = iter(range(10))
print(get_min_max(iterable))

iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))

iterable = iter([])
print(get_min_max(iterable))

data = iter([-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30])
print(get_min_max(data))