from functools import lru_cache

class Fibonacci:
    def __init__(self):
        self.n = 0
        self.i = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        fib_i = Fibonacci.fib(self.i)
        self.i += 1
        return fib_i
    
    @staticmethod
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        else:
            return Fibonacci.fib(n-1) + Fibonacci.fib(n-2)
        
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))