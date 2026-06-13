
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
    total_growth = 0
    growth_per_day = 0.8
    zucchini = plant("zucchini", 25, 22)
    zucchini.__show__()
    for day in range(1, 8):
        print(f"==Day {day}==")
        zucchini.grow(growth_per_day)
        zucchini.age(1)
        zucchini.__show__()
        total_growth += growth_per_day
    print(f"Total growth this week: {total_growth} cm")


if __name__ == "__main__":
    main()
