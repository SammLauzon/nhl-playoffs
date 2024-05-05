#!/usr/bin/env python3
"""Module that defines the script to calculate poolers point."""

import pathlib

from .pooler import Pooler
from .poolers import Poolers


def main() -> None:
    """Script main execution."""
    poolers_filepath = pathlib.Path('docs', 'poolers.md')
    ranking_filepath = pathlib.Path('docs', 'rankings.md')
    poolers = Poolers()
    poolers.set_rankings()
    with ranking_filepath.open('w', encoding='utf-8') as f:
        f.write('# Classement\n')
        f.write('Voici comment les points sont calculés pour cette année:\n\n')
        f.write("* 2 pts par victoire pour l'équipe choisie.\n")
        f.write("* +2 pts si l'équipe choisie est victorieuse.\n")
        f.write("* +3 pts si l'équipe choisie est victorieuse et que le nombre de matchs choisi est exact.\n")
        f.write('* Ceci donne donc un maximum de 13 points par série.\n\n')
    poolers.build_markdown_ranking(ranking_filepath)

    with poolers_filepath.open('w', encoding='utf-8') as f:
        f.write('# Choix Des Poolers\n\n')
    pooler: Pooler
    for pooler in sorted(poolers.poolers, key=lambda pooler: pooler.name):
        pooler.build_markdown_choices(poolers_filepath)


if __name__ == '__main__':
    main()
