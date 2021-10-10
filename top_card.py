from card import Card


class TopCard:
    def __init__(self, player_id=0, cards=Card(0, 'N')):
        amount = 0
        if cards is None:
            cards = [Card(0, 'N')]
        elif not isinstance(cards, list):
            cards = [cards]

        if isinstance(cards, Card):
            cards = [cards]

        if cards[0].value != 0:
            amount = len(cards)

        self.amount = amount
        self.cards = cards
        self.player_id = player_id
