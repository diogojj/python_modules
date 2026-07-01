#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._days: int = 0

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

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose")
    rose.set_height(15.0)
    rose.set_days(10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25.0)
    rose.set_days(30)

    rose.set_height(-5.0)
    rose.set_days(-1)

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
