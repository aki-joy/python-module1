class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        self.height += 0.8
        self.height = round(self.height, 1)

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    start_height = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        plant.show()

    total = round(plant.height - start_height, 1)
    print(f"Growth this week: {total}cm")
