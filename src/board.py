"""Static maze geometry: walls, legal moves, and precomputed shortest paths.

Emily's file (backend).

The board never changes during a game, so it is deliberately kept out of
GameState. That keeps the state small and cheap to copy, which matters a lot
once the solvers start expanding thousands of nodes.

The allPairs shortestPath table is computed once at load time. Both solvers'
evaluation functions lean on it heavily, and true maze distance is much better
than Manhattan distance. A hazard two cells away through a wall is not
actually a threat.
"""

from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from constants import HAZARD_CHAR, OPEN_CHAR, PLAYER_CHAR, WALL_CHAR, Action, Pos


@dataclass( frozen=True )
class Board:
    """Immutable maze geometry parsed from an ASCII layout."""

    height: int
    width: int
    walls: frozenset[Pos]
    open_cells: tuple[Pos, ...]
    playerStart: Pos
    hazardStarts: tuple[Pos, ...]

    # pos -> {otherPos: shortest path length in steps}. Unreachable pairs are
    # simply absent; use `distance()` rather than indexing this directly.
    _distances: dict[Pos, dict[Pos, int]]

    # construction
