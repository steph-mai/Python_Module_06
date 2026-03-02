# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 17:03:25 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 17:50:36 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import validate_ingredients
from alchemy.grimoire import record_spell


def ft_circular_curse() -> None:
    print("\n=== Circular Curse Breaking ===")

    try:
        print("\nTesting ingredient validation:")
        ingredients = "fire air"
        print(f"validate_ingredients(\"{ingredients}\"): "
              f"{validate_ingredients(ingredients)}")
        ingredients = "dragon scales"
        print(f"validate_ingredients(\"{ingredients}\"): "
              f"{validate_ingredients(ingredients)}")

        print("\nTesting spell recording with validation:")
        spell = "Fireball"
        ingredients = "fire air"
        print(f"record_spell(\"{spell}\", \"{ingredients}\"): "
              f"{record_spell(spell, ingredients)}")
        spell = "Dark Magic"
        ingredients = "shadow"
        print(f"record_spell(\"{spell}\", \"{ingredients}\"): "
              f"{record_spell(spell, ingredients)}")

        print("\nTesting late import technique:")
        spell = "Lightning"
        ingredients = "air"
        print(f"record_spell(\"{spell}\", \"{ingredients}\"): "
              f"{record_spell(spell, ingredients)}")
        print("\nCircular dependency curse avoided using late imports!")
        print("All spells processed safely!")

    except ImportError as e:
        print(f"\nError : Circular dependency or missing file: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    ft_circular_curse()
