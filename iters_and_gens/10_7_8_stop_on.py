def stop_on(iterable, obj):
    iterable = iter(iterable)
    for i in iterable:
        if i != obj:
            yield i
        else:
            break

numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))
