"""Transmutation 2: import the top-level alchemy package only."""
import alchemy


def main() -> None:
    """Run the recipe re-exported at the alchemy package level."""
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")


if __name__ == "__main__":
    main()
