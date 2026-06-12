class Plant:        
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = 0
        self.age = 0
        self.set_height(height, False)
        self.set_age(age, False)

    def set_height(self, height: int, show_message: bool = True) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            if show_message:
                print("Height update rejected")
            return
        self.height = height
        if show_message:
            print(f"Height updated: {self.height}cm")

    def set_age(self, age: int, show_message: bool = True) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if show_message:
                print("Age update rejected")
            return
        self.age = age
        if show_message:
            print(f"Age updated: {self.age} days")

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden security system ===")
    plan = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plan.name}: {plan.height}cm, {plan.age} days old")

    print("")
    plan.set_height(25)
    plan.set_age(30)
    plan.set_height(-10)
    plan.set_age(-5)
    print("Current state: ", end="")
    plan.show()
    