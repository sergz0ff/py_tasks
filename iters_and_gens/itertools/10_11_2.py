from itertools import groupby

words = input().split(' ')
groups = groupby(sorted(words, key=lambda x: (len(x), x)), key=lambda x: len(x))

for index, values in groups:
    print(
        f'{index} -> {", ".join(values)}'
    )