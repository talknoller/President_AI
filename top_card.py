from card import Card


class TopCard:
    def __init__(self, player_id=0, cards=list()):
        if isinstance(cards, Card):
            cards = [cards]

        self.amount = len(cards)
        self.cards = cards
        self.player_id = player_id
