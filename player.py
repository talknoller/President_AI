from card import Card
import utilites


class Player:
    def __init__(self, cards):
        self.cards = cards

    def available_moves(self, top_card):
        playable_cards = []

        if 1 == top_card.amount:
            for card in self.cards:
                if card.value >= top_card.cards[0].value:
                    playable_cards.append(card)

        if 2 == top_card.amount:
            pairs = find_pairs(self.cards)
            for pair in pairs:
                if pair[0].value >= top_card.cards[0].value:
                    playable_cards.append(pair)
