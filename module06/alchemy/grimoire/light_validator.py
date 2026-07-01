"""Light validator: safely imports the spellbook at module level."""
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients tagged VALID or INVALID."""
    allowed = light_spell_allowed_ingredients()
    found = any(item in ingredients.lower() for item in allowed)
    keyword = "VALID" if found else "INVALID"
    return f"{ingredients} - {keyword}"
