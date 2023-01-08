import functools
import time

def slow_down(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper

@slow_down
def countdown(number):
    if number < 1:
        print('Конец!')
    else:
        print(number)
        countdown(number - 1)
        
countdown(5)