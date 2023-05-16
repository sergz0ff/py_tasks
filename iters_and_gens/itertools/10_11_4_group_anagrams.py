from itertools import groupby

def group_anagrams(words):
    groups = groupby(
        sorted(words, key=lambda x: (len(x), sorted(list(x)))),
        key=lambda x: sorted(list(x))
    )
    return [tuple(group) for sign, group in groups]
    
groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

print(*groups)

