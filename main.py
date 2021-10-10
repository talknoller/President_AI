import random

from top_card import TopCard
from player import Player
import utilities
from card import Card
from node import Node


def create_players(number_of_players):
    hands = utilities.deal_cards(number_of_players)
    player_1 = Node(Player(hands[0], 1))
    next_player_node = player_1
    player_1.next_node = next_player_node

    for i in range(1, len(hands)):
        next_player_node.next_node = Node(Player(hands[i], i + 1))
        next_player_node = next_player_node.next_node

    next_player_node.next_node = player_1

    return next_player_node.next_node


def single_card_logic(player_node, top_card, players_left, number_of_winners, played_card, joker_value):
    if played_card.value == 0:
        print("player " + str(player_node.data.id) + " passed his turn")
        return turn(player_node.next_node, top_card, players_left, number_of_winners)

    if played_card.value == 2 or (played_card.value == 1 and joker_value == 2):
        print("player " + str(player_node.data.id) + " played " + str(played_card.value) + played_card.tie)
        player_node.data.cards.pop(played_card)
        return turn(player_node, TopCard(), players_left, number_of_winners)

    elif played_card.value == 1:
        print("player " + str(player_node.data.id) + " played " + str(played_card.value) + played_card.tie
              + " as " + str(joker_value))
        top_card = TopCard(player_node.data.id, Card(joker_value, played_card.tie))
        player_node.data.cards.pop(played_card)

    else:
        print("player " + str(player_node.data.id) + " played " + str(played_card.value) + played_card.tie)
        top_card = TopCard(player_node.id, played_card)
        player_node.data.cards.pop

    return turn(player_node.next_node, top_card, players_left, number_of_winners)


def turn(player_node, top_card, players_left, number_of_winners=0):
    if top_card.player_id == player_node.data.id:
        top_card = TopCard()
    played_cards = player_node.data.play_random_card(top_card)
    if isinstance(played_cards, Card):
        return single_card_logic(player_node, top_card, players_left, number_of_winners, played_cards, random.randint(2, 14))
    elif isinstance(played_cards, list):
        if len(played_cards) == 1:
            return single_card_logic(player_node, top_card, players_left, number_of_winners, played_cards[0], random.randint(2, 14))

    else:
        top_card = TopCard(cards=played_cards, player_id=player_node.data.id)
        for card in played_cards:
            player_node.data.cards.pop(utilities.find_card_index(player_node.data.cards, card))

        if player_node.data.cards is None or len(player_node.data.cards) == 0:
            print("player " + str(player_node.data.id) + " has won")
            return player_node
        return turn(player_node.next_node, top_card, players_left, number_of_winners)

    # if len(player_node.data.cards) == 0:
    #     player_node.data.result = number_of_winners + 1
    #     return turn(player_node.next, TopCard(), players_left - 1, number_of_winners + 1)
    #

    # if len(player_node.data.available_moves(top_card)) == 0:
    #     return turn(  )


players = create_players(5)

winner = turn(players, TopCard(), 5)
