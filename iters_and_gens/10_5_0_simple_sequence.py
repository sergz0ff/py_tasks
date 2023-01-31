def simple_sequence():
    num = 1
    while True:
        for i in range(num):
            yield num
        num += 1

generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)