import functools

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
               func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
print(say_beegeek.__name__)
print(say_beegeek.__doc__)
print('----------')
@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b
    
print(add.__name__)
print(add.__doc__)
print(add(10, b=20))