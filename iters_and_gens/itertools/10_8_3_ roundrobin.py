from itertools import zip_longest

def roundrobin(*args):
    for i in zip_longest(*args, fillvalue='filler'):
        for j in i:
            if j != 'filler':
                yield j


numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))

# 1 None 2 None 3 None None