class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
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

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden security system ===")
    Rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {Rose.name}: {Rose._height}cm, {Rose._age} days old")

    print("")
    Rose.set_height(25)
    Rose.set_age(30)
    Rose.set_height(-10)
    Rose.set_age(-5)
    print("Current state: ", end="")
    Rose.show()
