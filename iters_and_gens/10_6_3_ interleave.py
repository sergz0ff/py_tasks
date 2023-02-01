def interleave(*args):
    return (i
            for arg in zip(*args)
            for i in arg
            )


print(*interleave('bee', '123'))

# print(*zip('bee', '123'))