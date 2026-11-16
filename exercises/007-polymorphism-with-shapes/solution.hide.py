import math


# Don't modify the Shape class
class Shape:
    def area(self):
        raise NotImplementedError("Each shape must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def total_area(shapes):
    return round(sum(shape.area() for shape in shapes), 2)


shapes = [Rectangle(2, 3), Circle(1), Rectangle(1, 1)]
print(total_area(shapes))
