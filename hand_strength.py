from itertools import combinations
from collections import Counter

RANKS = '23456789TJQKA'

def hand_strength(hand):
    ranks = sorted([card[0] for card in hand], key=lambda r: RANKS.index(r), reverse=True)
    suits = [card[1] for card in hand]
    rc = Counter(ranks)
    is_flush = len(set(suits)) == 1
    is_straight = len(rc) == 5 and (RANKS.index(ranks[0]) - RANKS.index(ranks[-1]) == 4)
    if is_flush and is_straight: return (8, RANKS.index(ranks[0]))
    if 4 in rc.values(): return (7, rc.most_common(1)[0])
    if 3 in rc.values() and 2 in rc.values(): return (6, rc.most_common(1)[0])
    if is_flush: return (5, [RANKS.index(r) for r in ranks])
    if is_straight: return (4, RANKS.index(ranks[0]))
    if 3 in rc.values(): return (3, rc.most_common(1)[0])
    if list(rc.values()).count(2) == 2: return (2, rc.most_common(2))
    if 2 in rc.values(): return (1, rc.most_common(1)[0])
    return (0, [RANKS.index(r) for r in ranks])

def best_hand(seven):
    return max(combinations(seven, 5), key=hand_strength)