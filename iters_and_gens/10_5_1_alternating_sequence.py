def alternating_sequence(count=None):
    num = 1
    if count is None:
        while True:
            if num % 2:
                yield num
            else:
                yield num * -1
            num += 1
    else:
        while num <= count:
            if num % 2:
                yield num
            else:
                yield num * -1
            num += 1

generator = alternating_sequence()

print(next(generator))
print(next(generator))

generator = alternating_sequence(10)

print(*generator)