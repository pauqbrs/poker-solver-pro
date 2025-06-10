RANKS = '23456789TJQKA'
SUITS = 'cdhs'
FULL_DECK = [r + s for r in RANKS for s in SUITS]

def parse_cards(input_str, allow_ranges=False):
    cards = [c.strip() for c in input_str.split(',') if c.strip()]
    # TODO: ampliar para interpretar rangos como "JJ+,AQ+"
    return [cards] if len(cards) == 2 else [cards[i:i+2] for i in range(0, len(cards), 2)]