import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            try:
                if type(val) is datatype:
                    return val
                else:
                    raise TypeError
            except TypeError as err:
                raise err
        return wrapper
    return decorator

@returns(int)
def add(a, b):
    return a + b

try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))