def cyclic_shift(numbers: list[int | float], step: int) -> None:
    start: int = 0
    end: int = len(numbers) - 1
    if step > 0:
        for _ in range(step):
            numbers.insert(start, numbers.pop(end))
    elif step < 0:
        for _ in range(abs(step)):
            numbers.insert(end, numbers.pop(start))
    else:
        pass


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers)