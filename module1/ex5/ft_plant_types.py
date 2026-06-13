class plant:
    def __init__(self, name):
        self._name: str = name
        self._height: int = 0
        self._days: int = 0

    @classmethod
    def anonymous_plant(cls, name="anonymous plant"):
        return cls(name)

    def set_height(self, height):
        if height > 0:
            self._height = height
            print("Height updated")
        else:
            print("Height cannot be zero or negative\nheight update rejected.")

    def get_height(self):
        return self._height

    def set_days(self, days):
        if days > 0:
            self._days = days
            print("Days updated")
        else:
            print("Days cannot be zero or negative\n age update rejected.")

    def get_days(self):
        return self._days

    def __show__(self):
        print(f"{self._name}: {self._height} cm tall, {self._days} days old.")


class flower(plant):
    def __init__(self, name, color):
        super().__init__(name)
        self._color: str = color

    @classmethod
    def anonymous_plant(cls, name="anonymous flower", color="unknown"):
        return cls(name, color)

    def bloom(self):
        print(f"{self._name} is blooming with {self._color} petals!")

    def get_color(self):
        return self._color

    def __show__(self):
        super().__show__()
        print(f"Color: {self._color}")


class tree(plant):
    def __init__(self, name, trunk_diameter):
        super().__init__(name)
        self._trunk_diameter: int = trunk_diameter

    @classmethod
    def anonymous_plant(cls, name="anonymous tree", trunk_diameter=0):
        return cls(name, trunk_diameter)

    def get_trunk_diameter(self):
        return self._trunk_diameter

    def produce_shade(self):
        print(f"{self._name} now produces a shade with {self._height}cm height"
              f"and {self._trunk_diameter} diameter.")

    def __show__(self):
        super().__show__()
        print(f"Trunk Diameter: {self._trunk_diameter} cm")


class vegetable(plant):
    def __init__(self, name, harvest_season, nutritional_value):
        super().__init__(name)
        self._harvest_season: str = harvest_season
        self._nutritional_value: float = nutritional_value

    @classmethod
    def anonymous_plant(
        cls,
        name="anonymous vegetable",
        harvest_season="unknown",
        nutritional_value=0.0,
    ):
        return cls(name, harvest_season, nutritional_value)

    def get_nutritional_value(self):
        return self._nutritional_value

    def __show__(self):
        super().__show__()
        print(f"Harvest Season: {self._harvest_season}")
        print(f"Nutritional Value: {self._nutritional_value}")


def main():
    print("=== Plant Types Demo ===")
    print("==Creating a flower...")
    rose = flower("rose", "red")
    rose.set_height(15)
    rose.set_days(10)
    rose.__show__()
    print("asking flower to bloom")
    rose.bloom()

    print("==Creating an tree...")
    oak = tree("oak", 50)
    oak.set_height(200)
    oak.set_days(3650)
    oak.__show__()
    oak.produce_shade()

    print("==Creating a vegetable...")
    carrot = vegetable("carrot", "summer", 41.0)
    carrot.set_height(30)
    carrot.set_days(90)
    carrot.__show__()


if __name__ == "__main__":
    main()
