def find_pairs(cards):
    pairs = []
    for card in cards:
        for second_card in cards:
            if card.value == second_card. value and card.tie != second_card.tie:
                new_pair = [card, second_card]
                pairs.append(new_pair)

    return pairs


def find_triplets(cards):
    triplets = []
    pairs = find_pairs(cards)
    for pair in pairs:
        for card in cards:
            if card.value == pair[0].value and card.tie != pair[0].tie and card.tie != pair[1].tie
                pair.append(card)
                triplets.append(pair)
    return triplets