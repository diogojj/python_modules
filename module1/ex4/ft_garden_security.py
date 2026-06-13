class plant:
    def __init__(self, name):
        self._name: str = name
        self._height: int = 0
        self._days: int = 0

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


def main():
    print("===  Garden Security System ===")
    secret_plant = plant("plant 0")
    secret_plant.set_height(15)
    secret_plant.set_days(10)

    plant1 = plant("plant 1")
    plant1.set_height(-5)
    plant1.set_days(0)


if __name__ == "__main__":
    main()
