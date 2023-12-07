from sys import stdin
from collections import Counter

def card_strength(cards, joker=''):
    return [f'{joker}23456789TJQKA'.index(card) for card in cards]

def sort_by(cards_and_bid, joker=''):
    types = []
    for replace_j_with in ("23456789TQKA" if joker else 'J'):
        cards = cards_and_bid[0].replace('J', replace_j_with)
        types += [[c[1] for c in Counter(cards).most_common()]]

    return max(types), card_strength(cards_and_bid[0], joker)

def solve(joker=''):
    as_sorted = sorted(hands, key=lambda k: sort_by(k, joker))
    return sum(i * int(bid) for i, (cards, bid) in enumerate(as_sorted, 1))

hands = [line.split() for line in stdin.read().strip().split("\n")]

print(solve())
print(solve(joker='J'))
