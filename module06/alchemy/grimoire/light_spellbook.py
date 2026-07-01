
def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # Local import: executed only when this function runs, by which time
    # this module is already fully initialised -> no circular import.
    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if "INVALID" not in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
