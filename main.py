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


def turn(player_node, top_card):
    print(top_card.cards[0].value)
    if player_node.data.id == top_card.player_id:
        top_card = TopCard()
    played_card = player_node.data.play_random_card(top_card)

    if isinstance(played_card, Card):
        if played_card.value == 0:
            return turn(player_node.next_node, top_card)

    elif played_card[0].value == 0:
        return turn(player_node.next_node, top_card)

    if len(player_node.data.cards) == 0:
        return player_node

    if top_card.cards[0].value == played_card[0].value:
        if len(played_card) == 2:
            return turn(player_node, TopCard())
        return turn(player_node.next_node.next_node, TopCard(player_node.data.id, played_card))
    return turn(player_node.next_node, TopCard(player_node.data.id, played_card))


player_1 = Node(Player([Card(3, 'D'), Card(3, 'H'), Card(4, 'H')], 1))
player_2 = Node(Player([Card(3, 'B')], 2))
player_3 = Node(Player([Card(3, 'H')], 3))
player_4 = Node(Player([Card(3, 'C')], 4))
player_5 = Node(Player([Card(4, 'D')], 5))

player_1.next_node = player_2
player_2.next_node = player_3
player_3.next_node = player_4
player_4.next_node = player_5
player_5.next_node = player_1

players = create_players(5)
turn(player_1, TopCard(6, [Card(3, 'S'), Card(3, 'S')]))
