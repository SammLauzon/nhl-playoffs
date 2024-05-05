"""Module where all constants and enum class are defined."""

from dataclasses import dataclass
from enum import Enum


class Teams(Enum):
    """All teams defined in enum."""
    DAL = 1
    VGK = 2
    WPG = 3
    COL = 4
    VAN = 5
    NSH = 6
    EDM = 7
    LAK = 8
    FLA = 9
    TBL = 10
    BOS = 11
    TOR = 12
    NYR = 13
    WSH = 14
    CAR = 15
    NYI = 16


class Rounds(Enum):
    """Class defining all expected rounds."""
    RD1 = 'Round 1'
    RD2 = 'Round 2'
    RD3 = 'Round 3'
    RD4 = 'Round 4'


@dataclass
class Matchup:
    """Class defining the structure of a matchup"""
    round_encountered: Rounds
    result: dict[Teams, int]
    key: str

    def get_winner(self) -> Teams:
        """Found the winner using the result."""
        return max(self.result, key=self.result.get)

    def get_total_match(self) -> int:
        """Return the total number of match of the series."""
        return sum(self.result.values())


@dataclass
class Prediction:
    """Strcuture for a pooler predicitons"""
    matchup: Matchup
    winner: Teams
    nb_of_games: int


@dataclass
class Points:
    """Structure for points."""
    round1: int
    round2: int
    round3: int
    round4: int

    def get_total(self) -> int:
        """Calculate total points of a pooler."""
        return self.round1 + self.round2 + self.round3 + self.round4
