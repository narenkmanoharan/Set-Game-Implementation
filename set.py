import itertools
from enums import Color, Symbol, Shading
from card import Card


def create_cards(card_string):
    """
    Function takes in the card string from the file input and returns a Card object using the Class Card
    :rtype: Card Object
    """
    card = Card()
    card_string = card_string.split()
    if len(card_string) < 2:
        return
    card.color = getattr(Color, card_string[0])
    card.number = len(card_string[1]) - 1
    attribute = card_string[1]
    if attribute[0] == 'a' or attribute[0] == 'A' or attribute[0] == '@':
        card.symbol = Symbol.A
    elif attribute[0] == 's' or attribute[0] == 'S' or attribute[0] == '$':
        card.symbol = Symbol.S
    else:
        card.symbol = Symbol.H
    if attribute[0].istitle():
        card.shading = Shading.upper
    elif attribute[0].islower():
        card.shading = Shading.lower
    else:
        card.shading = Shading.symbol
    return card


def create_third_card(card1, card2):

    """
    Function to create the third card of a set when two cards are given
    :rtype: Card Object
    """
    card3 = Card()
    value_dict = {'01': 2, '10': 2, '12': 0, '21': 0, '20': 1, '02': 1}
    if card1.color == card2.color:
        card3.color = card2.color
    else:
        card3.color = value_dict[str(card1.color) + str(card2.color)]
    if card1.number == card2.number:
        card3.number = card2.number
    else:
        card3.number = value_dict[str(card1.number) + str(card2.number)]
    if card1.shading == card2.shading:
        card3.shading = card2.shading
    else:
        card3.shading = value_dict[str(card1.shading) + str(card2.shading)]
    if card1.symbol == card2.symbol:
        card3.symbol = card2.symbol
    else:
        card3.symbol = value_dict[str(card1.symbol) + str(card2.symbol)]
    return card3


def check_combination(cards):
    """
    Function to check if the combination is already in the found set else add it to the list
    :rtype: List of SETs (List of Lists)
    """
    result_set = []
    for each_combination in itertools.combinations(cards, 2):
        third_card = create_third_card(each_combination[0], each_combination[1])
        if third_card in cards:
            set_card = sorted([str(each_combination[0]), str(each_combination[1]), str(third_card)])
            if set_card not in result_set:
                result_set.append(set_card)
    return result_set


def find_largest_disjoint_set(cards):
    """
    Function to recursively find the disjoint SETs using the recurse_disjoint helper function
    :rtype: List of SETs (List of Lists)
    """
    largest_disjoint_set = []
    for result in recurse_disjoint(cards):
        if len(result) > len(largest_disjoint_set):
            largest_disjoint_set = result
    return largest_disjoint_set


def recurse_disjoint(set_of_cards, set_list=set(), memo=None):
    """
    Helper function to recursively check for disjoint set
    :rtype: Generator object
    """
    if memo is None:
        memo = []
    if memo:
        yield memo
    for i, x in enumerate(set_of_cards):
        if set_list.isdisjoint(x):
            for card in recurse_disjoint(set_of_cards[i + 1:], set_list | set(x), memo + [x]):
                yield card
