# =============================================================================
# ANOTHER CARD GAME — Scale AI Interview Question
# =============================================================================
#
# Build a standard 52-card deck and implement a two-player card game.
#
# STEP 1 — Build the deck
#   A standard deck has 52 cards:
#   - 4 suits: clubs, diamonds, hearts, spades
#   - 13 ranks per suit: 2 3 4 5 6 7 8 9 10 J Q K A  (low → high)
#
# STEP 2 — Implement two functions on the deck
#   - shuffle()  → randomize the order of cards in the deck
#   - draw()     → remove and return the top card
#
# STEP 3 — Play
#   - Create 2 players
#   - Each player draws 5 cards from the deck
#   - Each player finds their highest ranked card
#   - The player with the higher card wins
#   - If both highest cards are equal rank → tie
#
# EXAMPLE OUTPUT:
#   Player 1 hand: [('A','hearts'), ('3','clubs'), ('7','spades'), ('K','diamonds'), ('2','hearts')]
#   Player 2 hand: [('Q','clubs'), ('9','hearts'), ('J','spades'), ('5','diamonds'), ('10','clubs')]
#   Player 1 highest: A
#   Player 2 highest: Q
#   Player 1 wins!
#
# HINTS:
#   - Use a list of tuples (rank, suit) for cards
#   - Use random.shuffle() for the shuffle function
#   - Use an ORDER list to compare ranks: ORDER.index(rank)
#   - draw() should remove from one end of the deck (pop())
# =============================================================================

import pprint

import random

RANK_ORDER = ['2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['clubs',  'diamonds','hearts', 'spades']
class Deck:
    def __init__(self) -> None:
        self.cards = []
        
        for suit in SUITS:
            for rank in RANK_ORDER:
                self.cards.append((rank, suit))
        self.shuffle()
        
    def __repr__(self) -> str:
        return str(self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop(-1)
class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        for i in range(5):
            self.hand.append(self.deck.draw())
    def best_card(self):
        return max(self.hand, key =lambda x: RANK_ORDER.index(x[0]) )
     
class Game:
    def __init__(self, n1, n2, deck):
        self.p1 = Player(n1, deck)
        self.p2 = Player(n2, deck)
        pprint.pprint(f'player 1 {self.p1.hand}')
        pprint.pprint(f'player 2 {self.p2.hand}')
    def round(self):
        c1 = self.p1.best_card()
        c2 = self.p2.best_card()

        if RANK_ORDER.index(c1[0]) > RANK_ORDER.index(c2[0]):
            return f"{self.p1.name} won"
        elif RANK_ORDER.index(c1[0]) < RANK_ORDER.index(c2[0]):
            return  f"{self.p2.name} win"
        else:
            return "tie"

        
        
        
d = Deck()
d.shuffle()
# p1 = Player('a', d)
g = Game ('a', 'd', d)
pprint.pprint( g.round() )
        
