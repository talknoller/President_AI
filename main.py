from top_card import TopCard
from player import Player
import utilites
from card import Card
from node import Node


def create_players(number_of_players):
    hands = utilites.deal_cards(number_of_players)
    player_1 = Node(Player(hands[0], 1))
    next_player_node = player_1
    player_1.next_node = next_player_node

    for i in range(1, len(hands)):
        next_player_node.next_node = Node(Player(hands[i], i + 1))
        next_player_node = next_player_node.next_node

    next_player_node.next_node = player_1

    return next_player_node.next_node


players = create_players(5)
top_cards = [Card(3, 'S')]


# while len(players.data.cards) != 0:
#     if len(players.data.available_moves()) != 0:
#         players.data.play_random_card(top_cards)



