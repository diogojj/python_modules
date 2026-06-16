

class Plant:

    class Stats:

        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._days: int = 0
        self._stats: Plant.Stats = Plant.Stats()

    def set_height(self, height: float) -> None:
        if height > 0:
            self._height = height
            print("Height updated")
        else:
            print(f"{self._name}: Error, height can't be negative")
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
        self._stats.record_grow()

    def age(self, days: int) -> None:
        self._days += days
        self._stats.record_age()

    @staticmethod
    def is_year_old(days: int) -> bool:
        return days >= 365

    @classmethod
    def anonymous_plant(cls, name: str = "Unknown plant") -> "Plant":
        return cls(name)

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}: {self._height}cm, {self._days} days old")


class Flower(Plant):

    def __init__(self, name: str, color: str) -> None:
        super().__init__(name)
        self._color: str = color
        self._blooming: bool = False

    @classmethod
    def anonymous_plant(  # type: ignore[override]
        cls, name: str = "Unknown flower", color: str = "unknown"
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

    class TreeStats(Plant.Stats):

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, trunk_diameter: float) -> None:
        super().__init__(name)
        self._trunk_diameter: float = trunk_diameter
        self._stats: Tree.TreeStats = Tree.TreeStats()

    @classmethod
    def anonymous_plant(  # type: ignore[override]
        cls, name: str = "Unknown tree", trunk_diameter: float = 0.0
    ) -> "Tree":
        return cls(name, trunk_diameter)

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
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
        name: str = "Unknown vegetable",
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


class Seed(Flower):

    def __init__(self, name: str, color: str, seed_count: int = 0) -> None:
        super().__init__(name, color)
        self._seed_count: int = seed_count

    @classmethod
    def anonymous_plant(  # type: ignore[override]
        cls,
        name: str = "Unknown seed",
        color: str = "unknown",
        seed_count: int = 0,
    ) -> "Seed":
        return cls(name, color, seed_count)

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self._seed_count = seeds

    def get_seed_count(self) -> int:
        return self._seed_count

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")


def display_stats(plant: Plant) -> None:
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 40 days more than a year? -> {Plant.is_year_old(40)}")
    print(f"Is 370 days more than a year? -> {Plant.is_year_old(370)}")

    print("\n=== Flower")
    rose = Flower("Rose", "red")
    rose.set_height(15.0)
    rose.set_days(10)
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 5.0)
    oak.set_height(200.0)
    oak.set_days(365)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", "yellow")
    sunflower.set_height(80.0)
    sunflower.set_days(45)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom(seeds=42)
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous_plant()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)


if __name__ == "__main__":
    main()
