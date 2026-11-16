class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        return f"{self.brand} {self.model} with {self.wheels} wheels"


car = Car("Toyota", "Corolla")
print(car.description())
print(Car.wheels)
