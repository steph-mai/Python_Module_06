# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:25:26 by stmaire         #+#    #+#               #
#  Updated: 2026/03/02 15:12:24 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_pathway_debate() -> None:
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem

    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    from alchemy.transmutation.advanced import (
        philosophers_stone,
        elixir_of_life
    )

    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    import alchemy.transmutation
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    comparison = (
        "[same as above]"
        if alchemy.transmutation.philosophers_stone()
        == philosophers_stone()
        else "different"
    )
    print(f"alchemy.transmutation.philosophers_stone(): {comparison}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
