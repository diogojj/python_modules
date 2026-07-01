#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._days: int = 0

    @classmethod
    def anonymous_plant(cls, name: str = "anonymous plant") -> "Plant":
        return cls(name)

    def set_height(self, height: float) -> None:
        if height > 0:
            self._height = height
            print("Height updated")
        else:
            print(f"{self._name}: Error, height can't be negative or zero")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_days(self, days: int) -> None:
        if days > 0:
            self._days = days
            print("Days updated")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_days(self) -> int:
        return self._days

    def grow(self, amount: float) -> None:
        self._height = round(self._height + amount, 2)

    def age(self, days: int) -> None:
        self._days += days

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")


class Flower(Plant):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name)
        self._color: str = color
        self._blooming: bool = False

    @classmethod
    def anonymous_plant(  # type: ignore[override]
        cls, name: str = "anonymous flower", color: str = "unknown"
    ) -> "Flower":
        return cls(name, color)

    def bloom(self) -> None:
        self._blooming = True

    def get_color(self) -> str:
        return self._color

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, trunk_diameter: float) -> None:
        super().__init__(name)
        self._trunk_diameter: float = trunk_diameter

    @classmethod
    def anonymous_plant(  # type: ignore[override]
        cls, name: str = "anonymous tree", trunk_diameter: float = 0.0
    ) -> "Tree":
        return cls(name, trunk_diameter)

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        harvest_season: str,
        nutritional_value: float = 0.0,
    ) -> None:
        super().__init__(name)
        self._harvest_season: str = harvest_season
        self._nutritional_value: float = nutritional_value

    @classmethod
    def anonymous_plant(  # type: ignore[override]
        cls,
        name: str = "anonymous vegetable",
        harvest_season: str = "unknown",
        nutritional_value: float = 0.0,
    ) -> "Vegetable":
        return cls(name, harvest_season, nutritional_value)

    def get_nutritional_value(self) -> float:
        return self._nutritional_value

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self._nutritional_value += 1.0

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += 1.0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def main() -> None:
    print("=== Plant Types Demo ===")

    print("=== Flower")
    rose = Flower("Rose", "red")
    rose.set_height(15.0)
    rose.set_days(10)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 5.0)
    oak.set_height(200.0)
    oak.set_days(3650)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", "April")
    tomato.set_height(5.0)
    tomato.set_days(10)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age(1)
    tomato.show()


if __name__ == "__main__":
    main()

