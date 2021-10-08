import random
from card import Card


def create_deck():
    deck = []
    for i in range(2, 15):
        deck.append(Card(i, 'D'))

    for i in range(2, 15):
        deck.append(Card(i, 'H'))

    for i in range(2, 15):
        deck.append(Card(i, 'S'))

    for i in range(2, 15):
        deck.append(Card(i, 'C'))

    deck.append(Card(1, "R"))
    deck.append(Card(1, "B"))

    return deck


def find_pairs(cards):
    pairs = []
    for card in cards:
        for second_card in cards:
            if card.value == second_card.value and card.tie != second_card.tie and card.value != 2:
                new_pair = [card, second_card]
                pairs.append(new_pair)

    return pairs


def find_triplets(cards):
    triplets = []
    pairs = find_pairs(cards)
    for pair in pairs:
        for card in cards:
            if card.value == pair[0].value and card.tie != pair[0].tie and card.tie != pair[1].tie:
                pair.append(card)
                triplets.append(pair)
    return triplets


def find_quadrupoles(cards):
    quads = []
    triplets = find_triplets(cards)

    for triple in triplets:
        for card in cards:
            if card.value == triple[0].value and card.tie != triple[0].tie and card.tie != triple[1].tie and card.tie != \
                    triple[2].tie:
                triple.append(card)
                quads.append(triple)


def deal_cards(number_of_players):
    players = []
    for i in range(number_of_players):
        players.append(list())

    deck = create_deck()
    amount_of_cards = int(len(deck) / number_of_players)
    for player in players:
        for j in range(amount_of_cards):
            player.append(deck.pop(random.randint(0, len(deck) - 1)))

    for i in range(amount_of_cards % number_of_players):
        players[i].append(deck.pop(0))

    return players


def find_card_index(hand, card):
    for i in range(len(hand)):
        if hand[i] == card:
            return i
    return -1


def find_group_index(hand, group):
    for i in range(len(hand) - 1):
        if len(hand[i]) == len(group):
            is_there = True
            for card in group:
                if find_card_index(hand[i], card) == -1:
                    is_there = False
                    break

                else:
                    is_there = True

        if is_there:
            return i
    return -1


def find_card_by_value(cards, value):
    right_cards = []
    for card in cards:
        if card.value == value:
            right_cards.append(card)
    return right_cards


def find_jokers(cards):
    return find_card_by_value(cards, 1)


def find_cutters(cards):
    return find_card_by_value(cards, 2)
