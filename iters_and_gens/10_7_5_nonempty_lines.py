def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            if 0 < len(line.rstrip()) < 25:
                yield line
            if len(line.rstrip()) >= 25:
                yield '...'
