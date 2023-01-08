import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        try:
            if type(val) is str:
                return val
            else:
                raise TypeError
        except TypeError as err:
            raise err
    return wrapper


@returns_string
def beegeek():
    return 'beegeek'
    
print(beegeek())
print('---------')
@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))
print('---------')
@returns_string
def nothing():
    return

print(nothing.__name__)
print(nothing.__doc__)

try:
    nothing()
except TypeError as e:
    print(type(e))
