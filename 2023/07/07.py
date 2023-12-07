from sys import stdin
from collections import Counter

def sort_by(cards_and_bid, joker='_'):
    cards = cards_and_bid[0].replace(joker, "")
    types = [c[1] for c in Counter(cards).most_common()] or [0]
    types[0] += cards_and_bid[0].count(joker)
    strength = [f'{joker}23456789TJQKA'.index(card) for card in cards_and_bid[0]]
    return types, strength

def solve(joker=''):
    as_sorted = sorted(hands, key=lambda k: sort_by(k, joker))
    return sum(i * int(bid) for i, (cards, bid) in enumerate(as_sorted, 1))

hands = [line.split() for line in stdin.read().strip().split("\n")]

print(solve())
print(solve(joker='J'))
