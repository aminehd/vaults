# =============================================================================
# SURVIVAL CARD GAME — Scale AI Interview Question
# =============================================================================
#
# A team of players tries to survive Y rounds together.
#
# SETUP:
#   - Input: number of players, number of lives, number of skips, Y rounds
#   - Each player draws cards (assume infinite deck or pre-dealt)
#   - Each player's hand is always sorted ascending
#
# EACH ROUND:
#   - Players play in fixed order (Player 0, 1, 2, ...)
#   - Each player MUST play their SMALLEST available card
#   - The round is LOST if any card is NOT strictly greater than the previous card
#     e.g. Player 0 plays 3, Player 1 plays 3 → LOST (not strictly greater)
#     e.g. Player 0 plays 3, Player 1 plays 2 → LOST
#
# ON A LOST ROUND — team chooses one of:
#   - Lose a life  (lives -= 1)
#   - Use a skip   (skips -= 1, players draw NEW cards, round doesn't count)
#
# GAME OVER if: lives == 0 before completing all Y rounds
# WIN if: team completes all Y rounds
#
# SIMPLE STRATEGY (for simulation):
#   - Use a skip if skips > 0, otherwise lose a life
#
# OUTPUT: True if team survives, False if they lose
#
# EXAMPLE:
#   players=2, lives=3, skips=1, Y=3
#   cards dealt: Player0=[2,5,8], Player1=[3,6,9]
#
#   Round 1: P0 plays 2, P1 plays 3 → 3>2 ✓ → win
#   Round 2: P0 plays 5, P1 plays 6 → 6>5 ✓ → win
#   Round 3: P0 plays 8, P1 plays 9 → 9>8 ✓ → win
#   Result: True (survived all 3 rounds)
#
# TRICKIER EXAMPLE:
#   players=2, lives=1, skips=0, Y=2
#   cards dealt: Player0=[5,8], Player1=[3,9]
#
#   Round 1: P0 plays 5, P1 plays 3 → 3<5 → LOST
#   No skips → lose a life → lives=0
#   GAME OVER → False
#
# KEY INSIGHT:
#   Count how many rounds will be lost (non-increasing sequences).
#   If lost_rounds > skips + lives → team loses.
#
# CLASSES TO THINK ABOUT:
#   Player  — name, hand (sorted), play_card()
#   Game    — players, lives, skips, play_round(), play_game()
#
# =============================================================================

from dataclasses import dataclass, field
from typing import List
import random
import pprint
ORDER = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# hand is just a list of ints (rank indices) — no Card/Deck needed
# e.g. player.hand = [2, 5, 8]  means ranks '4', '7', '10'

@dataclass
class Player:
    name: str
    hand: List[int] = field(default_factory=list)  # list of ORDER indices, sorted

    def play_card(self):
        return self.hand.pop(0)  # always plays smallest (hand is sorted)
    def __repr__(self):
        return self.name + str(self.hand)
@dataclass
class Game:
    lives : int
    skip: int
    Y_rounds: int
    players: List[Player] = field(default_factory=list)
    def __post_init__(self) -> None:
        for i in range(4):
            p = Player(name=f'p{i}')
            self.players.append(p) 
        self._deal()
    def _deal(self):
        for p in self.players:
            p.hand = sorted( random.sample(range(13), self.Y_rounds + self.skip))
    def play_round(self):
        
        played = [p.play_card() for p in self.players]
        won = all(played[i] > played[i-1] for i in range(1, len(played)))

        if not won:
            if self.skip:
                self.skip -=1
            else:
                self.lives  -= 1
            self._deal()
        return won
    def play_game(self):
        while self.Y_rounds:
            won = self.play_round()
            if won: self.Y_rounds -= 1
    def __repr__(self) -> str:
        return str(self.players)


g = Game(lives=10, skip=2, Y_rounds =4)
print(g)
(g.play_game())