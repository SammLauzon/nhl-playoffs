"""Poolers predicitons regrouped."""

import pathlib

from dataclasses import dataclass

from .choices.round_1 import (SAMUEL_CHOICES_RD1, BRUNO_CHOICES_RD1, GILLES_CHOICES_RD1,
                              JULIEN_CHOICES_RD1, MIKAEL_CHOICES_RD1, MICHEL_CHOICES_RD1,
                              WILLIAM_CHOICES_RD1, STEVE_CHOICES_RD1, SYLVAIN_CHOICES_RD1,
                              PIERRE_CHOICES_RD1)
from .definitions import Rounds
from .pooler import Pooler


@dataclass
class Poolers:
    """Defined all poolers."""
    poolers = [Pooler('Samuel', {Rounds.RD1: SAMUEL_CHOICES_RD1,
                                 Rounds.RD2: None,
                                 Rounds.RD3: None,
                                 Rounds.RD4: None
                                 }),
               Pooler('Bruno', {Rounds.RD1: BRUNO_CHOICES_RD1,
                                Rounds.RD2: None,
                                Rounds.RD3: None,
                                Rounds.RD4: None
                                }),
               Pooler('Gilles', {Rounds.RD1: GILLES_CHOICES_RD1,
                                 Rounds.RD2: None,
                                 Rounds.RD3: None,
                                 Rounds.RD4: None
                                 }),
               Pooler('Michel', {Rounds.RD1: MICHEL_CHOICES_RD1,
                                 Rounds.RD2: None,
                                 Rounds.RD3: None,
                                 Rounds.RD4: None
                                 }),
               Pooler('Mikael', {Rounds.RD1: MIKAEL_CHOICES_RD1,
                                 Rounds.RD2: None,
                                 Rounds.RD3: None,
                                 Rounds.RD4: None
                                 }),
               Pooler('Julien', {Rounds.RD1: JULIEN_CHOICES_RD1,
                                 Rounds.RD2: None,
                                 Rounds.RD3: None,
                                 Rounds.RD4: None
                                 }),
               Pooler('William', {Rounds.RD1: WILLIAM_CHOICES_RD1,
                                  Rounds.RD2: None,
                                  Rounds.RD3: None,
                                  Rounds.RD4: None
                                  }),
               Pooler('Steve', {Rounds.RD1: STEVE_CHOICES_RD1,
                                Rounds.RD2: None,
                                Rounds.RD3: None,
                                Rounds.RD4: None
                                }),
               Pooler('Sylvain', {Rounds.RD1: SYLVAIN_CHOICES_RD1,
                                  Rounds.RD2: None,
                                  Rounds.RD3: None,
                                  Rounds.RD4: None
                                  }),
               Pooler('Pierre', {Rounds.RD1: PIERRE_CHOICES_RD1,
                                 Rounds.RD2: None,
                                 Rounds.RD3: None,
                                 Rounds.RD4: None
                                 })]

    def set_rankings(self) -> list[str]:
        """Calculate points and set rankings."""
        for pooler in self.poolers:
            pooler.calculate_points()
        self.poolers = sorted(self.poolers, key=lambda pooler: pooler.get_total_points(), reverse=True)

    def build_markdown_ranking(self, filepath: pathlib.Path) -> None:
        """Build the markdown rankings."""
        with filepath.open('a', encoding='utf-8') as f:
            f.write('| Pooler | RD1 | RD2 | RD3 | RD4 | Total |\n')
            f.write('| ------ | --- | --- | --- | --- | ----- |\n')
        pooler: Pooler
        for pooler in self.poolers:
            with filepath.open('a', encoding='utf-8') as f:
                f.write((f'| [{pooler.name}](./poolers.md#{pooler.name.lower()}) '
                         f'| {pooler.points.round1} | {pooler.points.round2} '
                         f'| {pooler.points.round3} | {pooler.points.round4} '
                         f'| {pooler.get_total_points()} |\n'))
