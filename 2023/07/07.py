from sys import stdin
from collections import Counter
from functools import partial

def lookup(card, j_is_joker=False):
    order = 'J23456789TQKA' if j_is_joker else '23456789TJQKA'
    return order.index(card)

def hand_type(occ):
    match sorted(occ.values(), reverse=True):
        case [5]: return 6
        case [4, _]: return 5
        case [3, 2]: return 4
        case [3, *_]: return 3
        case [2, 2, _]: return 2
        case [2, *_]: return 1
        case [*_]: return 0

def sort_by(cards_and_bid, j_is_joker=False):
    best = 0
    for j_replace in ("AKQT98765432" if j_is_joker else "J"):
        cards = cards_and_bid[0].replace('J', j_replace)
        best = max(best, hand_type(Counter(cards)))

    raw_strength = [lookup(card, j_is_joker) for card in cards_and_bid[0]]
    return best, raw_strength

hands = []
for line in stdin.read().strip().split("\n"):
    hands.append(line.split())

def solve(j_is_joker=False):
    as_sorted = sorted(hands, key=partial(sort_by, j_is_joker=j_is_joker))
    return sum(i * int(bid) for i, (cards, bid) in enumerate(as_sorted, 1))

print(solve(j_is_joker=False))
print(solve(j_is_joker=True))

