from datetime import date, timedelta

def dates(start, count=None):
    if count is None:
        while True:
            yield start
            if start == date.max:
                return
            start += timedelta(days=1)
    else:
        for i in range(count):
            yield start + timedelta(days=i)

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')