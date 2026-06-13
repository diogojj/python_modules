
class plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def __show__(self):
        print(f"{self.name}: {self.height} cm tall, {self.days} days old.")


def main():
    zucchini = plant("zucchini", 25, 22)
    zucchini.__show__()
    eggplant = plant("eggplant", 30, 30)
    eggplant.__show__()
    tomato = plant("tomato", 40, 40)
    tomato.__show__()


if __name__ == "__main__":
    main()
