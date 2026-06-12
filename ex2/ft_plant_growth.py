class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age = age_days


def show(plant: Plant):
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def glow(plant: Plant):
    plant.height += 0.8
    plant.height = round(plant.height, 1)


def age(plant: Plant):
    plant.age += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    total = 0
    print("=== Garden Plant Growth ===")
    show(plant)

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        glow(plant)
        age(plant)
        show(plant)
        total += 0.8

    total = round(total, 1)
    print(f"Growth this week: {total}cm")
