class CircleCalculator:
    pi = 3.14159

    @classmethod
    def calculate_area(cls, radius):
        return cls.pi * radius ** 2


print(CircleCalculator.calculate_area(5))
