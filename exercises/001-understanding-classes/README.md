# `001` Understanding Classes

A **class** is a blueprint to create **objects**. Each object (or **instance**) has its own data, called **attributes**, and can do actions, called **methods**.

```py
class Student:
    def __init__(self, name, age, grade):  # Runs when a new Student is created
        self.name = name  # Attributes
        self.age = age
        self.grade = grade

    def introduce(self):  # A method
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours):  # Another method that changes an attribute
        self.grade += hours * 0.5
        return self.grade


student1 = Student("Ana", 20, 80)
print(student1.introduce())  # Hello! I am Ana, I am 20 years old, and my current grade is 80.
print(student1.study(3))  # 81.5
```

`self` is the object itself: `self.name` means "the name of **this** student".

## 📝 Instructions:

1. Following the example, create a class called `Pet` whose `__init__` receives and stores `name`, `species` and `age`.

2. Add a method `describe()` that **returns** `"<name> is a <age> year old <species>."`

3. Add a method `birthday()` that increases `age` by `1` and **returns** the new age.

4. Create a pet and call its methods to see how they work.

## 📎 Example:

```py
luna = Pet("Luna", "cat", 3)
print(luna.describe())  # Luna is a 3 year old cat.
print(luna.birthday())  # 4
print(luna.describe())  # Luna is a 4 year old cat.
```

## 💡 Hint:

+ Every method receives `self` as its first parameter, even if you don't pass it when you call the method.
