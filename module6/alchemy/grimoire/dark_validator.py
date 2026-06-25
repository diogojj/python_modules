"""Dark validator: cursed with an eager circular dependency."""
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients tagged VALID or INVALID."""
    allowed = dark_spell_allowed_ingredients()
    found = any(item in ingredients.lower() for item in allowed)
    keyword = "VALID" if found else "INVALID"
    return f"{ingredients} - {keyword}"
