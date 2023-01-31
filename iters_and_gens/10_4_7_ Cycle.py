class Cycle:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        self

    def __next__(self):
        self.index += 1
        if self.index < len(self.iterable):
            return self.iterable[self.index]
        else:
            self.index = 0
            return self.iterable[self.index]




cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))