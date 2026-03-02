# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:49:07 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 15:59:13 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .basic import lead_to_gold, stone_to_gem
from .advanced import philosophers_stone, elixir_of_life

__all__ = [
        "lead_to_gold",
        "stone_to_gem",
        "philosophers_stone",
        "elixir_of_life"
     ]
