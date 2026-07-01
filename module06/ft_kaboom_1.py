"""Kaboom 1: dark magic explodes on a circular import."""


def main() -> None:
    """Try to use the cursed dark spellbook -> circular ImportError."""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    # from alchemy.grimoire.dark_spellbook import dark_spell_record

    # result = dark_spell_record("Necromancy", "bats and frogs")
    # print(f"Testing record dark spell: {result}")
    from alchemy.grimoire.light_spellbook import light_spell_record

    result = light_spell_record("Necromancy", "bats and frogs")
    print(f"Testing record dark spell: {result}")


if __name__ == "__main__":
    main()
