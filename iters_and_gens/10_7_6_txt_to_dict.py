def txt_to_dict():
    with open('iters_and_gens/planets.txt', 'r', encoding='utf-8') as file:
        content = file.read().split('\n\n')
        for line in content:
            line = line.split('\n')
            for i in range(len(line)):
                line[i] = tuple(line[i].split(' = '))
            yield dict(line)

planets = txt_to_dict()

print(next(planets))