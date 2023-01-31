class Alphabet:
    def __init__(self, language) -> None:
        self.alpha = {'ru': [chr(i) for i in range(1072, 1104)], 'en': [chr(i) for i in range(97, 123)]}
        self.alpha_count = len(self.alpha[language])
        self.act_alpha = self.alpha[language]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index < self.alpha_count:
            return self.act_alpha[self.index]
        else:
            self.index = 0
            return self.act_alpha[self.index]
        
en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)