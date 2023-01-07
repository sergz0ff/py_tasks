def do_twice(func):
    def wraper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wraper

# @do_twice
# def beegeek():
#     print('beegeek')
    
# beegeek()

@do_twice
def beegeek():
    print('beegeek')
    
print(beegeek())