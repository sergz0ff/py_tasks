import functools

def add_attrs(**kwargs_g):
    def decorator(func):
        func.__dict__.update(**kwargs_g)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_attrs(at1=10, at2=20, at3=30, at4=40, atf=50)
def add(a, b):
    '''add docs'''
    return a + b
    
print(add.at1)
print(add.at2)
print(add.at3)
print(add.__name__)
print(add.__doc__)
print(add(1, 2))
print(add(b=12, a=13))
print(add.at4)
print(add.atf)