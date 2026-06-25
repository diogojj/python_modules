"""Kaboom 0: light magic records a spell without exploding."""
from alchemy import grimoire


def main() -> None:
    """Record a light spell through the grimoire interface."""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result = grimoire.light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
