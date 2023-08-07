from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height


circle = Circle(10)
rectangle = Rectangle(15,10)

print(f"Area of Circle is : {circle.area()}")
print(f"Area of Rectangle is : {rectangle.area()}")
