class Square:
    def __init__(self, n) -> None:
        self.n = n
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.n:
            self.index += 1
            return self.index ** 2
        else:
            raise StopIteration 
        
squares = Square(10)

print(list(squares))