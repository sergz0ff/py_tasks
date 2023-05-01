def filter_names(names, ignore_char, max_names):
    no_numbs = (name for name in names if all(s.isalpha() for s in name))
    no_char = (name for name in no_numbs if ignore_char.lower() != name[0].lower())
    filtered = []
    for name in no_char:
        if len(filtered) < max_names:
            filtered.append(name)
    result = (name for name in filtered)
    return result
    # return (name for idx, name in enumerate(filtred_dig) if idx < max_names)


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))
