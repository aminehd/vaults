from dataclasses import dataclass, field
import pprint
import random
from typing import Any, List, Optional, Tuple

from unittest import suite

# =============================================================================
# IMPLEMENT A CARD GAME — Scale AI Interview Question
# =============================================================================
#
# A trick-taking card game with 4 players, 13 rounds.
#
# SETUP:
#   - Standard 52-card deck, shuffle and deal 13 cards to each player
#
# PART 1 — Play a trick (one round):
#   1. A selected player plays any card → this sets the "led suit"
#   2. Every other player MUST play a card of the led suit if they have one
#   3. If a player has NO card of the led suit → they may play any card
#   4. Print: "Player X played Card" for each player
#   5. Winner = player who played the HIGHEST rank of the led suit
#      (cards of other suits cannot win, even if higher rank)
#   6. Print the winner. Winner leads the next trick.
#
# PART 2 — Full game (13 rounds):
#   - Repeat Part 1 for 13 rounds until all cards are gone
#
# PART 3 — Fish point scoring:
#   Points are scored by the winner of each trick, for cards played in that trick:
#     5  → 5 fish points
#     10 → 10 fish points
#     K  → 10 fish points
#     all other cards → 0 points
#   At end of each round: print points winner collected
#   At end of game: print each player's total points
#   Print the player(s) with the highest total
#
# EXAMPLE ROUND:
#   Player 1 played 7♥  (leads, sets suit = hearts)
#   Player 2 played K♥  (follows suit)
#   Player 3 played 2♠  (no hearts → plays any)
#   Player 4 played 9♥  (follows suit)
#   Player 2 wins the trick! (K♥ highest heart)
#   Points this round: 10 (K=10pts)
#
# KEY RULES SUMMARY:
#   - Only cards of the LED SUIT can win
#   - Must follow suit if possible
#   - Highest rank of led suit wins (use ORDER for comparison)
#   - Fish points: 5→5, 10→10, K→10, else→0
#
# ORDER = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# =============================================================================

ORDER = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITS = ['hearts', 'clubs', 'diamonds', 'spades']
FISH_POINTS = {'5': 5, '10': 10, 'K': 10}

@dataclass
class Card:
    rank: str
    suit: str
    def __post_init__(self):
        self.value = ORDER.index(self.rank)
        self.fishpoint = FISH_POINTS.get(self.rank, 0)
    def __repr__(self):
        return f"card {self.rank} {self.suit}"
        
class Deck:
    def __init__(self):
        self.deck = []
        for rank in ORDER:
            for suit in SUITS:
                c = Card(rank, suit)
                self.deck.append(c)
        self.shuffle()
        
        
    def shuffle(self):
        random.shuffle(self.deck)
    def draw(self):
        return self.deck.pop(-1)
    def __repr__(self):
        return str(self.deck)


@dataclass
class Player:
    name: str
    hand: Optional[List[Card]] = field(default_factory=list) 
    score: int = 0
    def play_card(self, led_suit):
        card = None
        if led_suit is None:
            card = self.hand[0]
        else:
            matching = [c for c in self.hand if c.suit == led_suit]
            card = matching[0] if matching else self.hand[0]
        self.hand.remove(card)
        return card
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(f'name{i}') for i in range(4)]
        self.lead_player = self.players[0]
        for player in self.players:
            player.hand = self.deal(13)
        
        
    def deal(self, n):
        res = []
        for _ in range(n):
            res.append(self.deck.draw())
        return res
    def play_trick(self):
        played = []
        
        led_card = self.lead_player.play_card(led_suit=None)
        led_suit = led_card.suit
        played.append((self.lead_player , led_card )) 

        for player in self.players:
            if player == self.lead_player: continue;
            card = player.play_card(led_suit)
            played.append((player, card))
        
        for player, card in played:
            print(f"Player {player.name} played {card}")
            
        def filter_non_suit(x):
            player, card = x
            return card.suit == led_card.suit
        def sort_cards(x: Tuple(Player, Card)):
            return x[1].value
        played = list(filter( filter_non_suit, played ))
        played.sort( key = sort_cards, reverse=True)
        
        self.lead_player = played[0][0]
        
        points = sum(x[1].fishpoint for x in played)
        played[0][0].score = points
        print(f'{played[0][0].name} won with score {points}')
        return played
    def play_game(self):
        for _ in range(13):
            self.play_trick()
        
# pprint.pprint(d)

def test_player():
    p = Player(name='alice')
    p.hand = [Card('7','hearts'), Card('K','spades'), Card('2','hearts')]

    card = p.play_card('hearts')
    assert card.suit == 'hearts'
    assert len(p.hand) == 2

    card = p.play_card('clubs')   # no clubs → plays anything
    assert len(p.hand) == 1

def test_game():
    game = Game()
    # pprint.pprint(game.players[0].hand)
    game.players[0].hand =  [Card('5', 'clubs')]
    game.players[1].hand = [Card('4', 'clubs')] 
    game.players[2].hand = [Card('Q', 'clubs')] 
    game.players[3].hand = [Card('5', 'clubs')] 
    done = game.play_trick()
    assert game.lead_player, game.players[2]
    # pprint.pprint(done)

def test_play():
    game = Game()
    game.play_game()
    for player in game.players:
        pprint.pprint(player.score)
test_play()
print("player tests pass")