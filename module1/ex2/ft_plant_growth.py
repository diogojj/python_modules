#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def grow(self, growth: float) -> None:
        self.height = round(self.height + growth, 2)

    def age(self, days: int) -> None:
        self.days += days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    total_growth: float = 0.0
    growth_per_day: float = 0.8
    zucchini = Plant("zucchini", 25.0, 22)
    print("=== Garden Plant Growth ===")
    zucchini.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        zucchini.grow(growth_per_day)
        zucchini.age(1)
        zucchini.show()
        total_growth += growth_per_day
    print(f"Total growth this week: {round(total_growth, 2)}cm")


if __name__ == "__main__":
    main()
