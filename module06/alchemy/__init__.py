"""Public interface of the alchemy package.

Only a curated subset of names is re-exported here. Notably
``create_earth`` is intentionally NOT exposed, so reaching it through the
package raises AttributeError (and mypy complains) on purpose.
"""
from .elements import create_air
from .potions import healing_potion, strength_potion
from .transmutation.recipes import lead_to_gold

# Package-level alias of the healing potion.
heal = healing_potion

__all__ = [
    "create_air",
    "healing_potion",
    "strength_potion",
    "heal",
    "lead_to_gold",
]
