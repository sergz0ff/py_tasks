class Xrange:
    def __init__(self, start, end, step=1) -> None:
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step > 0:
            self.start += self.step
            if self.start < self.end:
                return self.start
            else:
                raise StopIteration
        else:
            self.start += self.step
            if self.start > self.end:
                return self.start
            else:
                raise StopIteration
        
xrange = Xrange(5, 10)

print(*xrange)