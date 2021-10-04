from card import Card
import utilites


class Player:
    def __init__(self, cards, name):
        self.cards = cards
        self.id = name

    def available_moves(self, top_card):
        pairs = utilites.find_pairs(self.cards)
        triplets = utilites.find_triplets(self.cards)
        quadrupoles = utilites.find_quadrupoles(self.cards)
        playable_cards = []

        if 0 == top_card.amount:
            for card in self.cards:
                if card.value != 2:
                    playable_cards.append(card)
            for pair in pairs:
                playable_cards.append(pair)
            for triple in triplets:
                playable_cards.append(triple)
            for quad in quadrupoles:
                playable_cards.append(quad)

        if 1 == top_card.amount:
            for card in self.cards:
                if card.value >= top_card.cards[0].value:
                    playable_cards.append(card)

        if 2 == top_card.amount:
            for pair in pairs:
                if pair[0].value >= top_card.cards[0].value:
                    playable_cards.append(pair)
        if 3 == top_card.amount:
            for triple in triplets:
                if triple[0].value >= top_card.cards[0].value:
                    playable_cards.append(triple)

