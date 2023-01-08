import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        name = func.__name__
        print (
            f'TRACE: вызов {name}() с аргументами: {args}, {kwargs}'
        )
        print (
            f'TRACE: возвращаемое значение {name}(): {repr(val)}'
        )
        return val
    return wrapper

# @trace
# def say(name, line):
#     return f'{name}: {line}'
    
# say('Jane', 'Hello, World')

# print('---------')

# @trace
# def sub(a, b, c):
#     '''прекрасная функция'''
#     return a - b + c
    
# print(sub.__name__)
# print(sub.__doc__)
# sub(20, 5, c=10)

@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek())    
print(beegeek.__name__)
print(beegeek.__doc__)