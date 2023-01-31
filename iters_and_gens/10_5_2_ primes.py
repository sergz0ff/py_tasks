def primes(left, right):
    step = 1
    while left <= right:
        counter = 0
        for i in range(1, left + 1):
            if left % i == 0:
                counter += 1
        if counter == 2:
            yield left
        left += step

generator = primes(1, 15)

print(*generator)

generator = primes(6, 36)

print(next(generator))
print(next(generator))