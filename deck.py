from card import Card


class Deck:
    def __init__(self):
        deck = []
        for i in range(2,14):
            deck.append(Card(i, 'D'))

        for i in range(2, 14):
            deck.append(Card(i, 'H'))

        for i in range(2, 14):
            deck.append(Card(i, 'S'))

        for i in range(2, 14):
            deck.append(Card(i, 'C'))

        deck.append(Card(1, "R"))
        deck.append(Card(1, "B"))

        self.deck = deck

