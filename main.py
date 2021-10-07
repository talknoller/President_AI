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


def turn(player_node, top_card, players_left, number_of_winners=0):
    # if len(player_node.data.cards) == 0:
    #     player_node.data.result = number_of_winners + 1
    #     return turn(player_node.next, TopCard(), players_left - 1, number_of_winners + 1)
    #
    if top_card.player_id == player_node.data.id:
        top_card = TopCard()


    # if len(player_node.data.available_moves(top_card)) == 0:
    #     return turn(  )


player_1_hand = []
for i in range(14):
    player_1_hand.append(Card(i, 'D'))

player_1 = Player(player_1_hand, 1)

