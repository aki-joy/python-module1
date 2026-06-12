class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 25.0, 30)
    Oak = Plant("Oak", 200.0, 365)
    Cactus = Plant("Cactus", 5.0, 90)
    Sunflower = Plant("Sunflower", 80.0, 45)
    Fern = Plant("Fern", 15.0, 120)

    plants = [Rose, Oak, Cactus, Sunflower, Fern]

    print("=== Plant Factory Output===")

    for plant in plants:
        print("Created: ", end="")
        plant.show()
