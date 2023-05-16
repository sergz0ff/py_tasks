def first_largest(iterable, number):
    for index, elem in enumerate(iterable):
        if elem > number:
            return index
    else:
        return -1


numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))