from math import ceil


def shuffle_cards(cards):
    half = ceil(len(cards) / 2)
    deck_1 = cards[0:half]
    deck_2 = cards[half:]
    final_deck = []
    for index in range(half):
        try:
            final_deck.append(deck_1[index])
            final_deck.append(deck_2[index])
        except IndexError:
            pass
    return final_deck
