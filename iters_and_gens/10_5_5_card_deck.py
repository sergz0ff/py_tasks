def card_deck(suit):
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    suits = ["пик", "треф", "бубен", "червей"]
    suits.remove(suit)
    while True:
        for s in suits:
            for value in values:
                yield ' '.join((value, s))

generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)