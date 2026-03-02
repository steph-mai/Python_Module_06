# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 16:42:11 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 17:47:49 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    checked_str = validate_ingredients(ingredients)

    if "- valid" in checked_str.lower():
        return f"Spell recorded: {spell_name} ({checked_str})"
    else:
        return f"Spell rejected: {spell_name} ({checked_str})"
