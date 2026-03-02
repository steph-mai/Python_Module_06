# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 11:38:44 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 13:32:19 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed with "
        f"{create_fire()} and {create_water()}"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with "
        f"{create_earth()} and {create_fire()}"
    )


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with "
        f"{create_air()} and {create_water()}"
    )


def wisdom_potion() -> str:
    return (
        f"Wisdom potion brewed with "
        f"{create_fire()}, {create_water()}"
        f"{create_earth()} and {create_air()}"
    )
