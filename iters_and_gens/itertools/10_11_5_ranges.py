from itertools import groupby

def ranges(numbers):
    groups = groupby(
        numbers,
        key=lambda x: x - numbers.index(x)
    )
    res = []
    for sign, nums in groups:
        temp = list(nums)
        res.append((temp[0], temp[-1]))
    return res

numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))