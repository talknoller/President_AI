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
        jokers = utilites.find_jokers(self.cards)

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
            if len(jokers) == 2:
                playable_cards.append(jokers)

        if 1 == top_card.amount:
            for card in self.cards:
                if card.value >= top_card.cards[0].value:
                    playable_cards.append([card])

        if 2 == top_card.amount:
            for pair in pairs:
                if pair[0].value >= top_card.cards[0].value:
                    playable_cards.append(pair)

            for card in self.cards:
                for joker in jokers:
                    if card.value >= top_card[0].value:
                        playable_cards.append([card, joker])

        if 3 == top_card.amount:
            for triple in triplets:
                if triple[0].value >= top_card.cards[0].value:
                    playable_cards.append(triple)

            for pair in pairs:
                if pair[0].value >= top_card.cards[0].value:
                    for joker in jokers:
                        pair.append(joker)
                        playable_cards.append(pair)

            if len(jokers) == 2:
                for card in self.cards:
                    if card.value >= top_card.cards[0].value:
                        triple = [card, joker[0], joker[1]]
                        playable_cards.append(triple)

        if 0 != top_card.amount:
            for cutter in utilites.find_cutters(self.cards):
                playable_cards.append([cutter])

        for joker in jokers:
            playable_cards.append([joker])

        return playable_cards

    def play_random_card(self, top_card):
        self.play_card(self.available_moves(top_card)[random.randint(0, len(self.available_moves(top_card)) - 1)],
                       top_card, 2)

    def play_card(self, cards, top_card, joker_value=0):
        if len(cards) == 1:
            if utilites.find_card_index(self.available_moves(top_card), cards) == -1:
                print("illegal play")
                return
            elif cards[0].value == 1:
                if top_card.cards[0].value <= joker_value <= 14 or joker_value == 2:
                    print("player " + str(self.id) + " played " + str(cards[0].value) + cards[0].tie +
                          " as " + str(joker_value))
                    return self.cards.pop(utilites.find_card_index(self.cards, cards[0]))
                else:
                    print("joker must have a value between " + str(top_card.cards[0].value) + " and 14 or 2")
                    return
            else:
                print("player " + str(self.id) + " played " + str(cards[0].value) + cards[0].tie)
                return self.cards.pop(utilites.find_card_index(self.cards, cards[0]))
        else:
            if utilites.find_group_index(self.available_moves(top_card), cards) == -1:
                print("illegal play")
                return
            else:
                played_cards = []
                print("player " + str(self.id) + " played " + str(len(cards)) + " cards:")
                for card in cards:
                    print(card.__str__())
                    played_cards.append(card)
                for card in played_cards:
                    self.cards.pop(utilites.find_card_index(self.cards, card))
                return played_cards
