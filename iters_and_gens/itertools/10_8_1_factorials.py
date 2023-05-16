from itertools import accumulate
import operator

def factorials(n):
    for i in accumulate(range(1, n+1), operator.mul):
        yield i

numbers = factorials(6)

print(*numbers)