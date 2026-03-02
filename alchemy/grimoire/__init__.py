# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 16:00:30 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 17:47:34 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .spellbook import record_spell
from .validator import validate_ingredients

__all__ = ["record_spell", "validate_ingredients"]
