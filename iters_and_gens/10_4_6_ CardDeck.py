class CardDeck:
    def __init__(self) -> None:
        self.card_name = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.card_suit = ("пик", "треф", "бубен", "червей")
        self.card_name_index = -1
        self.card_suit_index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.card_suit_index < len(self.card_suit):
            self.card_name_index += 1
            if self.card_name_index < len(self.card_name):
                return ' '.join((self.card_name[self.card_name_index], self.card_suit[self.card_suit_index]))
            else:
                self.card_suit_index += 1
                self.card_name_index = 0
                if self.card_suit_index < len(self.card_suit):
                    return ' '.join((self.card_name[self.card_name_index], self.card_suit[self.card_suit_index]))
                else:
                    raise StopIteration
        else:
            raise StopIteration

cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])