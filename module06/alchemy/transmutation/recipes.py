"""Recipes mixing absolute and relative imports to reach the same goal."""
from ..potions import strength_potion       # relative import
from alchemy.elements import create_air     # absolute import
import elements                             # absolute import (root module)


def lead_to_gold() -> str:
    """Transmute lead into gold by mixing air, a strength potion and fire."""
    air = create_air()
    strength = strength_potion()
    fire = elements.create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and "
        f"'{strength}' mixed with '{fire}'"
    )
