"""Shared configuration: board layouts, scoring rules, and level definitions.

Shared responsibility (Emily and Allison). Nothing in here executes game logic. 
it is data so that the frontend, the engine, and both solvers all agree on
the same rules.
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

# A position is always (row, col). row 0 is the top of the board.
Pos = tuple[int, int]

class Action( Enum ) :
    """The five moves available to the player and to a hazard."""

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    STAY = (0, 0)

    @property
    def delta(self) -> Pos :
        return self.value

    def applyTo( self, pos: Pos ) -> Pos :
        return ( pos[0] + self.value[0], pos[1] + self.value[1] )


class Outcome( Enum ) :
    """How an episode ended. ONGOING means it has not ended yet."""

    ONGOING = "ongoing"
    WIN = "win"          # collected the target number of gems
    CAUGHT = "caught"    # a hazard reached the player
    TIMEOUT = "timeout"  # ran out of turns

    @property
    def isTerminal( self ) -> bool :
        return self is not Outcome.ONGOING

    @property
    def isWin( self ) -> bool :
        return self is Outcome.WIN


# Board characters used in the ASCII layouts below

WALL_CHAR = "#"
OPEN_CHAR = "."
PLAYER_CHAR = "P" # draft
HAZARD_CHAR = "H" # draft

# Scoring

GEM_SCORE = 10        # reward for collecting one gem
STEP_COST = 1         # charged every turn, so dawdling is penalised
CAUGHT_PENALTY = 100  # charged once if a hazard catches the player
WIN_BONUS = 50        # awarded once for collecting the target gems

# Value returned by the evaluation function for terminal states. Must be larger
# in magnitude than any reachable heuristic score so search never prefers a
# heuristic guess over a real win.
TERMINAL_WIN_VALUE = 10_000
TERMINAL_LOSS_VALUE = -10_000

# draft 1
CLASSIC_MAZE = """
###################
#H.......#.......H#
#.##.###.#.###.##.#
#.................#
#.##.#.#####.#.##.#
#....#...#...#....#
###.##.#.#.#.##.###
#........#........#
#.##.###.#.###.##.#
#........P........#
###################
"""

OPEN_ARENA = """
#############
#H.........H#
#..#.....#..#
#...........#
#..#..#..#..#
#.....P.....#
#############
"""


@dataclass( frozen=True )
class Level :
    """One reproducible experiment configuration.

    The seed is what makes the environment "random but repeatable". Two
    solvers run on the same level see the exact same gem spawns and the exact
    same hazard dice rolls, which is what makes the comparison fair.
    """

    name: str
    layout: str
    seed: int
    maxTurns: int = 120
    targetGems: int = 12

    # Hazard behaviour. With probability hazardChaseProb a hazard steps
    # toward the player; if not then it picks uniformly among its legal moves.
    # This is the whole point of the project: Minimax assumes the hazard always
    # plays the worst move for us, while Expectimax trusts this distribution.
    hazardChaseProb: float = 0.7
    hazardsMayStay: bool = False

    # Gem spawning.
    initialGems: int = 6
    gemSpawnProb: float = 0.25  # chance of one new gem per turn
    maxGemsOnBoard: int = 10

    # Search default, overridable from the command line.
    searchDepth: int = 3


LEVELS: dict[str, Level] = {
    "classic": Level(
        name="classic" ,
        layout=CLASSIC_MAZE ,
        seed=20260729 ,
    ) ,
    # Small board, few walls: hazards corner you fast, so the cautious/greedy
    # split between the two solvers shows up much more sharply here.
    "arena": Level(
        name="arena" ,
        layout=OPEN_ARENA ,
        seed=1337 ,
        max_turns=80 ,
        target_gems=8 ,
        initial_gems=4 ,
        max_gems_on_board=6 ,
    ) ,
}

DEFAULT_LEVEL = "classic"
