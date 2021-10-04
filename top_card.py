from card import Card


class TopCard:
    def __init__(self, cards):
        self.cards = cards
        self.amount = len(cards)
