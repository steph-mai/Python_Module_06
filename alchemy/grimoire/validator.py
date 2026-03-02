# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 16:05:42 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 17:51:12 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    valid_ingredients: list[str] = ["fire", "water", "earth", "air"]

    words = ingredients.lower().split()
    is_valid = any(ingredient in words for ingredient in valid_ingredients)

    if is_valid is True:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
