import random

ACHIEVEMENTS: list[str] = [
    "Dragon Tamer", "Night Owl", "Combo King", "Loot Goblin",
    "Flawless Run", "Map Maker", "Quick Draw", "Iron Will",
    "Ghost Walker", "Pixel Perfect", "Last Stand", "Treasure Diver",
    "Shield Bearer", "Time Bender",
]


def gen_player_achievements() -> set[str]:
    """Pick a random amount of unique achievements and return them."""
    amount: int = random.randint(6, 11)
    picked: list[str] = random.sample(ACHIEVEMENTS, amount)
    return set(picked)


def main() -> None:
    """Build several players' achievement sets and compare them."""
    print("=== Achievement Tracker System ===")
    players: list[str] = ["Nora", "Theo", "Mila", "Owen", "Ivy"]
    rosters: dict[str, set[str]] = {}
    for name in players:
        rosters[name] = gen_player_achievements()
        print(f"Player {name}: {rosters[name]}")

    distinct: set[str] = set()
    for owned in rosters.values():
        distinct = distinct.union(owned)
    print(f"All distinct achievements: {distinct}")

    common: set[str] = distinct
    for owned in rosters.values():
        common = common.intersection(owned)
    print(f"Common achievements: {common}")

    for name in players:
        others: set[str] = set()
        for other_name in players:
            if other_name != name:
                others = others.union(rosters[other_name])
        only: set[str] = rosters[name].difference(others)
        print(f"Only {name} has: {only}")

    for name in players:
        missing: set[str] = distinct.difference(rosters[name])
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
