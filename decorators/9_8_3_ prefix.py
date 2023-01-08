import functools

def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            if to_the_end:
                return val + string
            else:
                return string + val
        return wrapper
    return decorator

@prefix('€')
def get_bonus():
    return '2000'
    
print(get_bonus())

@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
       
print(get_bonus())