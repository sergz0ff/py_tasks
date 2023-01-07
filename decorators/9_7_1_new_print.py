old_print = print

def new_print(*args, sep=" ", end='\n'):
    sep = sep.upper()
    end = end.upper()
    args = [i.upper() if type(i) is str else i for i in args]
    old_print(*args, sep=sep, end=end)

print = new_print

print('hi', 'there', end='!')