class Animal:
    def __init__(self, species):
        self.species = species

    def makeSound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def makeSound(self):
        return "Woof woof ..."

class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name

    def makeSound(self):
        return "Meow meow ..."

dog = Dog("Seru")
cat = Cat("Whiskers")

print(f"{dog.name} the {dog.species} says: {dog.makeSound()}")
print(f"{cat.name} the {cat.species} says: {cat.makeSound()}")


