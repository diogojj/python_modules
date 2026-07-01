import random


def main() -> None:
    """Use list and dict comprehensions to transform player data."""
    print("=== Game Data Alchemist ===")
    players: list[str] = [
        "nora", "Theo", "mila", "Owen", "Ivy", "liam", "Zoe", "raj",
    ]
    print(f"Initial list of players: {players}")

    all_caps: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps: list[str] = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_caps}")

    scores: dict[str, int] = {
        name: random.randint(50, 1000) for name in all_caps
    }
    print(f"Score dict: {scores}")

    average: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high: dict[str, int] = {
        name: value for name, value in scores.items() if value > average
    }
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
