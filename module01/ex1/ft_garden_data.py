#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    zucchini = Plant("zucchini", 25, 22)
    zucchini.show()
    eggplant = Plant("eggplant", 30, 30)
    eggplant.show()
    tomato = Plant("tomato", 40, 40)
    tomato.show()


if __name__ == "__main__":
    main()
