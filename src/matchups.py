"""Defining matchups and round"""

from .definitions import Matchup, Rounds, Teams


class Matchups:
    """All matchup grouped in a class."""
    DAL_VGK = Matchup(round_encountered=Rounds.RD1, result={Teams.DAL: 3, Teams.VGK: 3}, key='DAL vs VGK')  # NOT FINISHED
    WPG_COL = Matchup(round_encountered=Rounds.RD1, result={Teams.WPG: 1, Teams.COL: 4}, key='WPG vs COL')
    VAN_NSH = Matchup(round_encountered=Rounds.RD1, result={Teams.VAN: 4, Teams.NSH: 2}, key='VAN vs NSH')
    EDM_LAK = Matchup(round_encountered=Rounds.RD1, result={Teams.EDM: 4, Teams.LAK: 1}, key='EDM vs LAK')
    FLA_TBL = Matchup(round_encountered=Rounds.RD1, result={Teams.FLA: 4, Teams.TBL: 1}, key='FLA vs TBL')
    BOS_TOR = Matchup(round_encountered=Rounds.RD1, result={Teams.BOS: 4, Teams.TOR: 3}, key='BOS vs TOR')
    NYR_WSH = Matchup(round_encountered=Rounds.RD1, result={Teams.NYR: 4, Teams.WSH: 0}, key='NYR vs WSH')
    CAR_NYI = Matchup(round_encountered=Rounds.RD1, result={Teams.CAR: 4, Teams.NYI: 1}, key='CAR vs NYI')
