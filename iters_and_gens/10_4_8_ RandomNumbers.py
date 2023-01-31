from random import randint

class RandomNumbers:
    def __init__(self, left, right, n) -> None:
        self.n = n
        self.left = left
        self.right = right

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return randint(self.left, self.right)
        else:
            raise StopIteration
        
iterator = RandomNumbers(-1000, -900, 1)
print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')