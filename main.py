from top_card import top_card
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

    for i in range(10):
        print(next_player_node.data.id)
        next_player_node = next_player_node.next_node


create_players(5)




