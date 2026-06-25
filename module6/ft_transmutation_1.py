"""Transmutation 1: import the transmutation sub-package."""
from alchemy import transmutation


def main() -> None:
    """Run the recipe exposed by the transmutation package interface."""
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()
