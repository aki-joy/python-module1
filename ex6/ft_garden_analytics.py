class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self._stats = Plant.Statistics()
        self.set_height(height, False)
        self.set_age(age, False)

    def set_height(self, height: float, show_message: bool = True) -> None:
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

    def grow(self) -> None:
        self._height += 0.8
        self._height = round(self._height, 1)
        self._stats.add_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.add_age()

    def shade(self) -> None:
        self._stats.add_shade()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats.add_show()

    class Statistics:
        def __init__(self) -> None:
            self._count_grow = 0
            self._count_age = 0
            self._count_show = 0
            self._count_shade = 0

        def add_grow(self) -> None:
            self._count_grow += 1

        def add_age(self) -> None:
            self._count_age += 1

        def add_shade(self) -> None:
            self._count_shade += 1

        def add_show(self) -> None:
            self._count_show += 1

        def show_stats(self) -> None:
            print(f"Stats: {self._count_grow} grow, {self._count_age} age, "
                  f"{self._count_show} show")

        def show_shade_stats(self) -> None:
            print(f" {self._count_shade} shade")

    def show_statistics(self) -> None:
        self._stats.show_stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def make_anonymous(cls) -> "Plant":
        return cls("Unknown", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.is_blooming:
            print(f"{self.name} has not bloomed yet")
        elif self.is_blooming:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.is_blooming = True


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def show_statistics(self) -> None:
        super().show_statistics()
        self._stats.show_shade_stats()

    def produce_shade(self) -> None:
        super().shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 season: str, nutrition: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = nutrition

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()

    def grow_and_age(self, days: int) -> None:
        for i in range(0, days):
            self.grow()
            self.age()

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def display_statistics(plant: Plant) -> None:
    print(f"--- Statistics for {plant.name} ---")
    plant.show_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print(f"[statistics for {flower.name}]")
    flower.show_statistics()
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    print(f"[statistics for {flower.name}]")
    flower.show_statistics()

    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5)
    tree.show()
    print(f"[statistics for {tree.name}]")
    tree.show_statistics()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print(f"[statistics for {tree.name}]")
    tree.show_statistics()

    print("\n=== Seed")
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow()
    seed.age()
    seed.bloom()
    seed.show()
    print(f"[statistics for {seed.name}]")
    seed.show_statistics()

    print("\n=== Anonymous")
    anonymous = Plant.make_anonymous()
    anonymous.show()
    print(f"[statistics for {anonymous.name}]")
    anonymous.show_statistics()
