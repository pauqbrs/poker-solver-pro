import random
from itertools import combinations
from hand_strength import hand_strength, best_hand
from utils import FULL_DECK

def evaluate(hole, board):
    return hand_strength(best_hand(hole + board))

def monte_carlo_equity(hero, villain_list, board=[], iterations=5000):
    wins, ties = 0, 0
    for _ in range(iterations):
        deck = [c for c in FULL_DECK if c not in hero + board]
        for v in villain_list:
            deck = [c for c in deck if c not in v]
        sample = random.sample(deck, 5 - len(board))
        full_board = board + sample

        hero_score = evaluate(hero, full_board)
        villain_scores = [evaluate(v, full_board) for v in villain_list]
        max_v = max(villain_scores)

        if hero_score > max_v:
            wins += 1
        elif hero_score == max_v:
            ties += 1
    total = iterations
    return wins / total, ties / total