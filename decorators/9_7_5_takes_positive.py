def takes_positive(func):
    def wrapper(*args, **kwargs):
        try:
            for i in args:
                if type(i) is not int:
                    raise TypeError
                if i <= 0:
                    raise ValueError
            for i in kwargs.values():
                if type(i) is not int:
                    raise TypeError
                if i <= 0:
                    raise ValueError
        except (TypeError, ValueError) as err:
            return type(err)
        else:
            return func(*args, **kwargs)
    return wrapper

@takes_positive
def positive_sum(*args):
    return sum(args)
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))