def all_together(*args):
    return (
        i 
        for arg in args
        for i in arg
    )

objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))