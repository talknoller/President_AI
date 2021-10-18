import random

from top_card import TopCard
from player import Player
import utilities
from card import Card
from node import Node


def create_players(number_of_players):
    hands = utilities.deal_cards(number_of_players)
    player = Node(Player(hands[0], 1))
    next_player_node = player
    player.next_node = next_player_node

    for i in range(1, len(hands)):
        next_player_node.next_node = Node(Player(hands[i], i + 1))
        next_player_node = next_player_node.next_node

    next_player_node.next_node = player

    return next_player_node.next_node


def turn(player_node, top_card, revolution_counter=0):
    if len(player_node.data.cards) == 0:
        return player_node
    elif player_node.data.cards is None:
        return player_node

    if player_node.data.id == top_card.player_id:
        print("deck got cut")
        top_card = TopCard()
    played_card = player_node.data.play_most_cards(top_card)

    if isinstance(played_card, Card):
        if played_card.value == 0:
            return turn(player_node.next_node, top_card)
        elif played_card.value == 2:
            return turn(player_node, TopCard())

    elif isinstance(played_card, list):
        if len(played_card) == 4:
            print("revolution")
            return turn(player_node, TopCard())
        if played_card[0].value == 0:
            return turn(player_node.next_node, top_card)
        elif played_card[0].value == 2:
            return turn(player_node, TopCard())

        if len(player_node.data.cards) == 0:
            return player_node

        if top_card.cards[0].value == played_card[0].value:
            if len(played_card) == 2:
                print("revolution")
                return turn(player_node, TopCard())

            if (revolution_counter + 1) == 4:
                print("revolution")
                return turn(player_node, TopCard())

            print("player " + str(player_node.next_node.data.id) + " got skipped")
            return turn(player_node.next_node.next_node, TopCard(player_node.data.id, played_card),
                        revolution_counter + 1)
    return turn(player_node.next_node, TopCard(player_node.data.id, played_card))


def full_game(number_of_players):
    players = create_players(number_of_players)
    for i in range(number_of_players):
        print("player " + str(players.data.id) + " hand")
        for card in players.data.cards:
            print(str(card.value) + card.tie)
        print("\n")
        players = players.next_node
    winners = list()
    for i in range(number_of_players - 1):
        winner = turn(players, TopCard())
        print(str(winner.data.id) + " won")
        winner.data.result = 'W'
        winners.append(winner)
        while players.next_node.data.result != 'W':
            players = players.next_node
        players.next_node = players.next_node.next_node
        players = players.next_node
    print("player " + str(players.data.id) + " is the asshole")
    winners.append(players)
    return winners


players_by_win_order = full_game(5)
for player in players_by_win_order:
    print(player.data.id)
