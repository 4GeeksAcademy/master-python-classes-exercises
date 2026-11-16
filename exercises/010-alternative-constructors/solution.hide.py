class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name, int(age))

    @classmethod
    def from_birth_year(cls, name, birth_year, current_year):
        return cls(name, current_year - birth_year)


ana = Person.from_string("Ana,25")
print(ana.name, ana.age)
leo = Person.from_birth_year("Leo", 2000, 2026)
print(leo.name, leo.age)
