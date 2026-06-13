class plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def grow(self, growth):
        self.height = round(self.height + growth, 2)

    def age(self, days):
        self.days += days

    def __show__(self):
        print(f"{self.name}: {self.height} cm tall, {self.days} days old.")


def main():
    print("=== Welcome to the Plant Factory ===")
    rose = plant("rose", 15, 10)
    print(f"created: {rose.__show__()}")
    tulip = plant("tulip", 10, 5)
    print(f"created: {tulip.__show__()}")
    sunflower = plant("sunflower", 20, 12)
    print(f"created: {sunflower.__show__()}")
    daisy = plant("daisy", 5, 2)
    print(f"created: {daisy.__show__()}")
    eggplant = plant("eggplant", 30, 30)
    print(f"created: {eggplant.__show__()}")


if __name__ == "__main__":
    main()
