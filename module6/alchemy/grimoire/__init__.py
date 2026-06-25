"""Grimoire interface: only the safe light spells are exposed."""
from .light_spellbook import (
    light_spell_allowed_ingredients,
    light_spell_record,
)

__all__ = [
    "light_spell_allowed_ingredients",
    "light_spell_record",
]
