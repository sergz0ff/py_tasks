def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            return (None, 'При вызове функции произошла ошибка')
        else:
            return (func(*args, **kwargs), 'Функция выполнилась без ошибок')
    return wrapper

sum = exception_decorator(sum)

print(sum(['199', '1', 187]))

@exception_decorator
def f(x):
    return x**2 + 2*x + 1
    
print(f(7))