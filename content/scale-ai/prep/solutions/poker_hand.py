# =============================================================================
# POKER HAND — Scale AI Interview Question
# =============================================================================
#
# INPUT: a hand = list of 5 tuples → [('rank', 'suit'), ...]
#   rank: '2' '3' '4' '5' '6' '7' '8' '9' '10' 'J' 'Q' 'K' 'A'  (low→high)
#   suit: 'hearts' 'spades' 'clubs' 'diamonds'
#
# GOAL: check which poker patterns the hand matches
#
# THE 6 PATTERNS (ranked best→worst):
#
#   royal flush    → 10 J Q K A all same suit         ('10','h'),('J','h'),('Q','h'),('K','h'),('A','h')
#   straight flush → 5 consecutive ranks, all same suit  5h 6h 7h 8h 9h
#   four of a kind → 4 cards same rank                   K K K K 2
#   full house     → 3 of one rank + 2 of another        K K K A A
#   flush          → all 5 same suit, any ranks          2h 7h 9h Jh Kh
#   straight       → 5 consecutive ranks, any suit       5h 6s 7c 8d 9h
#
# DESIGN: PokerHand class
#   __init__ precomputes self.ranks, self.suits, self.counts (Counter)
#   primitives: is_flush, is_straight  ← implement these
#   combos reuse primitives:
#     is_straight_flush = is_flush AND is_straight
#     is_royal_flush    = is_flush AND ranks == {10,J,Q,K,A}
#     is_four_of_a_kind = any count == 4
#     is_full_house     = counts have a 3 and a 2
#
# KEY TOOLS:
#   Counter(ranks)         → {'K':3, 'A':2}  ← use for full house / four of a kind
#   set(suits)             → {'hearts'}       ← len==1 means flush
#   RANK_ORDER.index(rank) → int position     ← use to check consecutive for straight
# =============================================================================

from collections import Counter

RANK_ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

sample_flush         = [('2','hearts'), ('7','hearts'), ('9','hearts'), ('J','hearts'), ('K','hearts')]
sample_straight      = [('5','hearts'), ('6','spades'), ('7','clubs'), ('8','diamonds'), ('9','hearts')]
sample_full_house    = [('K','hearts'), ('K','spades'), ('K','clubs'), ('A','hearts'), ('A','spades')]
sample_four_of_kind  = [('K','hearts'), ('K','spades'), ('K','clubs'), ('K','diamonds'), ('2','hearts')]
sample_straight_flush= [('5','hearts'), ('6','hearts'), ('7','hearts'), ('8','hearts'), ('9','hearts')]
sample_royal_flush   = [('10','hearts'), ('J','hearts'), ('Q','hearts'), ('K','hearts'), ('A','hearts')]
sample_nothing       = [('2','hearts'), ('5','spades'), ('7','clubs'), ('9','diamonds'), ('J','hearts')]

samples = [
    sample_flush       , 
    sample_straight      ,
    sample_full_house    ,
    sample_four_of_kind  ,
    sample_straight_flush,
    sample_royal_flush   ,
    sample_nothing       ,
 
]
ORDER = ['2', '3', '4', '5', 
         '6', '7', '8', '9', '10', 
         'J', 'Q', 'K', 'A' ]
class PokerHand:
    def __init__(self, hand):
        self.hand = hand
        self.ranks = [card[0] for card in hand]
        self.suits = [card[1] for card in hand]
        self.num_jokers = Counter(self.ranks)['J']
        self.rank_order =  [ORDER.index(x) for x in self.ranks]
        self.rank_order.sort()
        self.rank_count = Counter(self.rank_order)
        self.no_joker = list(filter( lambda x :x != ORDER.index('J'), self.rank_order))
        self.suit_counts = Counter(self.suits)

    # primitives
    def is_flush(self):
        print(self.suit_counts) 
        return  len ( self.suit_counts.values()   ) == 1
    
    # def is_straight(self):
    #     return len(set(self.rank_order)) == 5 and self.rank_order[-1] - self.rank_order[0] == 5
    
    # combos built from primitives
    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_royal_flush(self):
        return self.is_flush() and set(self.ranks) == {'10','J','Q','K','A'}
    def is_four_of_kind(self):
        return 4 in self.rank_count.values() or 5 in self.rank_count.values()
    def is_full_house(self):
        # pdb.set_trace()
        return set(self.rank_count.values()) == {2, 3}
    def is_full_house_joker(self):
        # pdb.set_trace()
        counts = sorted(Counter(self.no_joker).values(), reverse=True)
        num_jockers = self.num_jokers
        if not counts:
            return False

        if counts[0] + num_jockers < 3:
            return False
    
        jocker_used = max(0, 3 - counts[0])
        remaining_jocker = num_jockers - jocker_used
        if len(counts) > 1:
            
            return counts[1] + remaining_jocker == 2
        else:
            return remaining_jocker == 2
        
        
        
    def is_straight_with_joker(self):
        gap = 0
        for i in range(len(self.no_joker)):
            if i == 0:
                continue
            new_gap = self.no_joker[i] - self.no_joker[i-1]  
            if new_gap == 0: return False;
            gap += new_gap - 1
            
        # pdb.set_trace()
        return gap <= self.rank_count[ORDER.index('J')]
            
            

# tests = ['is_straight_with_joker']
tests = ['is_full_house_joker']

s1 = [('5','hearts'), ('7','spades'), ('8','clubs'), ('9','diamonds'), ('9','hearts')]
s2 = [('5','hearts'), ('6','spades'), ('7','clubs'), ('8','diamonds'), ('9','hearts')]
s3 = [('5','hearts'), ('5','spades'), ('J','clubs'), ('J','diamonds'), ('9','hearts')]

samples = [s3]
import pdb

for sample in samples:
    p = PokerHand(sample)
    # pdb.set_trace()  # execution stops here — inspect p.ranks, p.rank_order, p.suit_counts
    for fn in tests:
        print(f'for sample {sample} and {fn}')
        print(f"{fn}: {getattr(p, fn)()}")
    