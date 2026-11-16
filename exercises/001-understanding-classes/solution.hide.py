class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def describe(self):
        return f"{self.name} is a {self.age} year old {self.species}."

    def birthday(self):
        self.age += 1
        return self.age


luna = Pet("Luna", "cat", 3)
print(luna.describe())
print(luna.birthday())
print(luna.describe())
