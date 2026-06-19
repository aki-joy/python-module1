class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height, False)
        self.set_age(age, False)

    def set_height(self, height: int, show_message: bool = True) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            if show_message:
                print("Height update rejected")
            return
        self._height = height
        if show_message:
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int, show_message: bool = True) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if show_message:
                print("Age update rejected")
            return
        self._age = age
        if show_message:
            print(f"Age updated: {self._age} days")

    def grow(self):
        self._height += 0.8
        self._height = round(self._height, 1)

    def age(self):
        self._age += 1

    @staticmethod
    def is_year_old(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if not self.is_blooming:
            print(f"{self.name} has not bloomed yet")
        elif self.is_blooming:
            print(f"{self.name} is blomming beutifully!")

    def bloom(self):
        self.is_blooming = True


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int,
                 color: str, seed_count: int):
        super().__init__(name, height, age, color)
        self._seed_count = 0
        self._bloomed_seed_count = seed_count


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, nutrition: int):
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = nutrition

    def grow_and_age(self, days: int):
        for i in range(0, days):
            super().grow()
            super().age()
            self.nutritional_value += 1

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Flower")
    flower.show()
    flower.bloom()
    print("[asking the rose to bloom]")
    flower.show()
    print("\n=== Tree")
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("\n=== Vegetable")
    vegetable.show()
    days = 20
    print(f"[make the {vegetable.name} grow and age for {days} days]")
    vegetable.grow_and_age(days)
    vegetable.show()
