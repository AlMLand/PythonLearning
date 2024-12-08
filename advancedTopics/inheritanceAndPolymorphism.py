class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sound(self):
        print(f"{self.name} a sound")

    def walk(self):
        print(f"{self.name} is walking")

    def run(self):
        print(f"{self.name} is running")


# Dog inherited Animal
class Dog(Animal):
    def eat(self):
        print(f"{self.name} Dog override the eat method")


# Cat inherited Animal
class Cat(Animal):
    def eat(self):
        print(f"{self.name} Cat override the eat method")


class SomeService:
    def print_eating_text(self, animal: Animal):
        animal.eat()


service = SomeService()
service.print_eating_text(Dog("Aa"))
service.print_eating_text(Cat("Bb"))
