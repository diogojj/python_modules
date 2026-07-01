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
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 15.0, 10)
    print("Created: ", end="")
    rose.show()
    tulip = Plant("tulip", 10.0, 5)
    print("Created: ", end="")
    tulip.show()
    sunflower = Plant("sunflower", 20.0, 12)
    print("Created: ", end="")
    sunflower.show()
    daisy = Plant("daisy", 5.0, 2)
    print("Created: ", end="")
    daisy.show()
    eggplant = Plant("eggplant", 30.0, 30)
    print("Created: ", end="")
    eggplant.show()


if __name__ == "__main__":
    main()
