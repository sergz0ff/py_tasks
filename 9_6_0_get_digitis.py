def get_digits(number: int | float) -> list[int]:
    res: list[int] = []
    for c in str(number):
        if c != '.':
            res.append(int(c))
    return res


print(get_digits(16733))
print(get_digits(13.909934))

annotations = get_digits.__annotations__
print(annotations['return'])