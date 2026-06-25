"""Light spellbook: breaks the cycle with a deferred (local) import."""


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell after validating its ingredients."""
    # Local import: executed only when this function runs, by which time
    # this module is already fully initialised -> no circular import.
    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if "INVALID" not in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
