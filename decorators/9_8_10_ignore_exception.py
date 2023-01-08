import functools

def ignore_exception(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                if type(err) in types:
                    print(
                        f'Исключение {type(err).__name__} обработано'
                    )
                else:
                    raise err
        return wrapper
    return decorator

@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    return 'beegeek'
    
print(beegeek())