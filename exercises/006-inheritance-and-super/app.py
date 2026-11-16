# Don't modify the Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours):
        return f"{self.name} is studying for {hours} hours."


# Create the CollegeStudent class below
