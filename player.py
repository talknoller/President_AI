from card import Card
import utilities
import random


class Player:
    def __init__(self, cards, name):
        self.cards = cards
        self.id = name
        self.result = 'N'

    def available_moves(self, top_card):
        pairs = utilities.find_pairs(self.cards)
        triplets = utilities.find_triplets(self.cards)
        quadrupoles = utilities.find_quadrupoles(self.cards)
        playable_cards = []
        jokers = utilities.find_jokers(self.cards)

        if 0 == top_card.amount:
            for card in self.cards:
                if card.value != 2:
                    playable_cards.append(card)
            for pair in pairs:
                playable_cards.append(pair)
            for triple in triplets:
                playable_cards.append(triple)
            if quadrupoles is not None:
                for quad in quadrupoles:
                    playable_cards.append(quad)
            if len(jokers) == 2:
                playable_cards.append(jokers)

        if 1 == top_card.amount:
            for card in self.cards:
                if card.value >= top_card.cards[0].value:
                    playable_cards.append([card])
            only_cutters = True
            for card in playable_cards:
                if card[0].value != 2:
                    only_cutters = False
            if only_cutters:
                return []

        if 2 == top_card.amount:
            for pair in pairs:
                if pair[0].value >= top_card.cards[0].value:
                    playable_cards.append(pair)

            for card in self.cards:
                for joker in jokers:
                    if card.value >= top_card.cards[0].value:
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
                        triple = [card, jokers[0], jokers[1]]
                        playable_cards.append(triple)

        if 0 != top_card.amount:
            for cutter in utilities.find_cutters(self.cards):
                playable_cards.append([cutter])

        for joker in jokers:
            playable_cards.append([joker])

        return playable_cards

    def play_random_card(self, top_card):
        joker_value = random.randint(top_card.cards[0].value, 15)
        if joker_value == 15:
            joker_value = 2
        chosen_card_index = random.randint(0, (len(self.available_moves(top_card))))
        return self.play_chosen_card(top_card, chosen_card_index, joker_value)

    def play_chosen_card(self, top_card, chosen_card_index, joker_value=2):
        if joker_value < top_card.cards[0].value:
            joker_value = 2

        played_cards_list = list()
        playable_moves = self.available_moves(top_card)
        if playable_moves is None or len(playable_moves) == 0:
            print("player " + str(self.id) + " passes his turn")
            return [Card(0, 'N')]
        if chosen_card_index == len(playable_moves):
            print("player " + str(self.id) + " passes his turn")
            return [Card(0, 'N')]

        message = ""
        if isinstance(playable_moves[chosen_card_index], Card):
            message = "player " + str(self.id) + " played: " + str(self.available_moves(top_card)[chosen_card_index].value) + \
                      self.available_moves(top_card)[chosen_card_index].tie

            if playable_moves[chosen_card_index].value == 1:
                print(message + " as " + str(joker_value))
                joker = self.cards.pop(chosen_card_index)
                joker.value = joker_value
                return joker

        elif isinstance(playable_moves[chosen_card_index], list):
            message = "player " + str(self.id) + " played: " \
                      + str(self.available_moves(top_card)[chosen_card_index][0].value) + \
                      self.available_moves(top_card)[chosen_card_index][0].tie
            if playable_moves[chosen_card_index][0].value == 1:
                message += " as " + str(joker_value)
                playable_moves[chosen_card_index][0].value = joker_value

        if isinstance(playable_moves[chosen_card_index], Card):

            print(message)
            return self.cards.pop(chosen_card_index)

        else:
            played_cards_string = ''
            played_cards_value = 1
            for card in playable_moves[chosen_card_index]:
                played_cards_list.append(card)
                if card.value != 1:
                    played_cards_value = card.value
            for card in played_cards_list:
                self.cards.pop(utilities.find_card_index(self.cards, card))
                if card.value == 1:
                    card.value = played_cards_value
                played_cards_string += str(card.value) + card.tie + " "

            if len(playable_moves[chosen_card_index]) == 1:
                print(message)
            if len(playable_moves[chosen_card_index]) == 2:
                print("player " + str(self.id) + " played a pair: " + played_cards_string)

            elif len(playable_moves[chosen_card_index]) == 3:
                print("player " + str(self.id) + " played a triple: " + played_cards_string)

            elif len(playable_moves[chosen_card_index]) == 4:
                print("player " + str(self.id) + " played a quadruple: " + played_cards_string)
            elif len(playable_moves[chosen_card_index]) >= 5:
                print("too many cards played")
                return [Card(0, 'N')]
            return played_cards_list

    def play_most_cards(self, top_card):
        max_value = 0
        max_index = 0
        for i in range(len(self.available_moves(top_card))):
            if isinstance(self.available_moves(top_card)[i], list):
                if len(self.available_moves(top_card)[i]) > max_value:
                    max_value = len(self.available_moves(top_card)[i])
                    max_index = i
        return self.play_chosen_card(top_card, max_index)
