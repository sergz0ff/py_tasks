import functools

def takes(*args_g):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if type(arg) not in args_g:
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))
print('-' * 20)
@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))
