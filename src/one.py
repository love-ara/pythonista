
class Human:
    number_of_eyes = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def sleep(self):
        print("sleeping...")

    def eat(self):
        print("eating...")

    def __str__(self):
        return f"{self.name} {self.gender}"


h1 = Human(5, "male", "Ade")
h2 = Human(6, "female", "Asa")


print(h1.number_of_eyes)
print(h2.number_of_eyes)
print(h1.sleep())
print(h1.eat())
print(h2)
