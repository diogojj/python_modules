"""Distillation 1: 'import alchemy' to reach potions and the heal alias."""
import alchemy


def main() -> None:
    """Brew through the package interface, using the heal() alias."""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
