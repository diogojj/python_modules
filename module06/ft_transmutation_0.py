"""Transmutation 0: import the recipes module directly."""
import alchemy.transmutation.recipes as recipes


def main() -> None:
    """Run the recipe by importing recipes.py through its package path."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {recipes.lead_to_gold()}")


if __name__ == "__main__":
    main()
