"""Defining a pooler class."""

import pathlib

from .definitions import Points, Prediction, Rounds
from .matchups import Matchups


class Pooler:
    """Structure of a pooler"""

    def __init__(self, name: str, predictions: dict[Rounds, list[Prediction]]) -> None:
        """Initialize class member."""
        self.name = name
        self.predictions = predictions
        self.points = Points(0, 0, 0, 0)

    def calculate_points(self) -> None:
        """Calculate the total points of a pooler for each round."""
        victory_points = 2  # Points per victory of chosen team.
        good_team_bonus = 2  # Good team
        perfect_prediciton_points = 3  # Good match and good team.

        # Calculate based on predictions.
        for round, predictions in self.predictions.items():
            round_points = 0
            if predictions is None:
                continue
            for prediction in predictions:
                # Skip vegas for now.
                if prediction.matchup == Matchups.DAL_VGK:
                    continue
                points = 0
                points += victory_points * prediction.matchup.result[prediction.winner]
                if prediction.matchup.get_winner() == prediction.winner:
                    points += good_team_bonus
                    if prediction.matchup.get_total_match() == prediction.nb_of_games:
                        points += perfect_prediciton_points
                round_points += points

            if round == Rounds.RD1:
                self.points.round1 = round_points
            elif round == Rounds.RD2:
                self.points.round2 = round_points
            elif round == Rounds.RD3:
                self.points.round3 = round_points
            elif round == Rounds.RD4:
                self.points.round4 = round_points

    def get_total_points(self) -> int:
        """Calculate total points of a pooler."""
        return self.points.get_total()

    def build_markdown_choices(self, filepath: pathlib.Path) -> None:
        """Build markdown file for each pooler"""
        with filepath.open('a', encoding='utf-8') as f:
            f.write(f'## {self.name.title()}\n')
        for round, predictions in self.predictions.items():
            if predictions is None:
                continue
            with filepath.open('a', encoding='utf-8') as f:
                f.write(f'=== "{round.value}"\n')
                f.write('\t| Affrontement | Choix | Nombre de matchs |\n')
                f.write('\t| ------------ | ----- | ---------------- |\n')
            for prediction in predictions:
                with filepath.open('a', encoding='utf-8') as f:
                    f.write(f'\t| {prediction.matchup.key} | {prediction.winner.name} | {prediction.nb_of_games} |\n')

            with filepath.open('a', encoding='utf-8') as f:
                f.write('\n')

        with filepath.open('a', encoding='utf-8') as f:
            f.write('\n')
