from card import Card
import utilites
import random


class Player:
    def __init__(self, cards, name):
        self.cards = cards
        self.id = name
        self.result = 'N'

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
                    playable_cards.append([card])
            for joker in utilites.find_jokers(self.cards):
                playable_cards.append(joker)

        if 2 == top_card.amount:
            for pair in pairs:
                if pair[0].value >= top_card.cards[0].value:
                    playable_cards.append(pair)
        if 3 == top_card.amount:
            for triple in triplets:
                if triple[0].value >= top_card.cards[0].value:
                    playable_cards.append(triple)

        return playable_cards

    def play_random_card(self, top_card):
        playable_cards = self.available_moves(top_card)
        chosen_cards = playable_cards[random.randint(0, len(playable_cards) - 1)]
        for card in chosen_cards:
            for i in range(len(self.cards) - 1):
                if self.cards[i] == card:
                    self.cards.pop(i)

        print("player number " + str(self.id) + " played ")
        print(chosen_cards[0].__str__())
