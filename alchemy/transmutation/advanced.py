# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:44:33 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 15:04:07 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return (
        f"Philosopher's stone created using {lead_to_gold()} "
        f"and {healing_potion()}"
        )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
