import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            res = ''
            if len(val[end:]) + 1 >= end - start:
                res = val[:start] + char * (end - start) + val[end:]
            else:
                res = val[:start] + char * (len(val) - start)
            return res
        return wrapper
    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'
    
print(beegeek())
print('-------')
@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'
    
print(beegeek())
print('------')
@strip_range(20, 30)
def beegeek():
    return 'beegeek'
    
print(beegeek())
print('-------------')
@strip_range(0, 4, '=')
def beegeek():
    return 'beegeek'
    
print(beegeek())