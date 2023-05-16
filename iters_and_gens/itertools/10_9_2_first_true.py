from itertools import islice

def first_true(iterable, predicate):
    if predicate == None:
        predicate = bool
    for i in islice(filter(predicate, iterable), 0,1):
        return i

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))