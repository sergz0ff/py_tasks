def reverse_args(func):
    def wrapper(*args):
        return func(*args[::-1])
    return wrapper

@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))

@reverse_args
def concat(a, b, c):
    return a + b + c
    
print(concat('apple', 'cherry', 'melon'))