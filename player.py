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
            for cutter in utilities.find_cutters(self.cards):
                playable_cards.append([cutter])

        for joker in jokers:
            playable_cards.append([joker])

        return playable_cards

    def play_random_card(self, top_card):
        joker_value = random.randint(2, 14)
        played_cards_list = list()
        playable_moves = self.available_moves(top_card)
        chosen_cards = random.randint(0, len(playable_moves))
        if playable_moves is None or len(playable_moves) == 0:
            print("player " + str(self.id) + " passes his turn")
            return [Card(0, 'N')]
        if chosen_cards == len(playable_moves):
            print("player " + str(self.id) + " passes his turn")
            return [Card(0, 'N')]

        message = ""
        if isinstance(playable_moves[chosen_cards], Card):
            message = "player " + str(self.id) + " played: " + str(self.available_moves(top_card)[chosen_cards].value) +\
                  self.available_moves(top_card)[chosen_cards].tie
        elif isinstance(playable_moves[chosen_cards], list):
            message = "player " + str(self.id) + " played: " + str(self.available_moves(top_card)[chosen_cards][0].value) +\
                  self.available_moves(top_card)[chosen_cards][0].tie

        if isinstance(playable_moves[chosen_cards], Card):
            if playable_moves[chosen_cards].value == 1:
                print(message + " as " + str(joker_value))
                joker = self.cards.pop(chosen_cards).value = joker_value
                return joker

            print(message)
            return self.cards.pop(chosen_cards)

        else:
            played_cards_string = ''
            for card in playable_moves[chosen_cards]:
                played_cards_list.append(card)

            for card in played_cards_list:
                self.cards.pop(utilities.find_card_index(self.cards, card))
                if card.value == 1:
                    card.value = joker_value
                played_cards_string += str(card.value) + card.tie + " "

            if len(playable_moves[chosen_cards]) == 1:
                print(message)
            if len(playable_moves[chosen_cards]) == 2:
                print("player " + str(self.id) + " played a pair: " + played_cards_string)

            elif len(playable_moves[chosen_cards]) == 3:
                print("player " + self.id + " played a triple: " + played_cards_string)

            elif len(playable_moves[chosen_cards]) == 4:
                print("player " + self.id + " played a quadruple: " + played_cards_string)
            elif len(playable_moves[chosen_cards]) >= 5:
                print("too many cards played")
                return [Card(0, 'N')]
            return played_cards_list


    # def play_card(self, cards, top_card, joker_value=0):
    #     if len(cards) == 1:
    #         if utilites.find_card_index(self.available_moves(top_card), cards) == -1:
    #             print("illegal play")
    #             return
    #         elif cards[0].value == 1:
    #             if top_card.cards[0].value <= joker_value <= 14 or joker_value == 2:
    #                 print("player " + str(self.id) + " played " + str(cards[0].value) + cards[0].tie +
    #                       " as " + str(joker_value))
    #                 return self.cards.pop(utilites.find_card_index(self.cards, cards[0]))
    #             else:
    #                 print("joker must have a value between " + str(top_card.cards[0].value) + " and 14 or 2")
    #                 return
    #         else:
    #             print("player " + str(self.id) + " played " + str(cards[0].value) + cards[0].tie)
    #             return self.cards.pop(utilites.find_card_index(self.cards, cards[0]))
    #     else:
    #         if utilites.find_group_index(self.available_moves(top_card), cards) == -1:
    #             print("illegal play")
    #             return
    #         else:
    #             played_cards = []
    #             print("player " + str(self.id) + " played " + str(len(cards)) + " cards:")
    #             for card in cards:
    #                 print(card.__str__())
    #                 played_cards.append(card)
    #             for card in played_cards:
    #                 self.cards.pop(utilites.find_card_index(self.cards, card))
    #             return played_cards
