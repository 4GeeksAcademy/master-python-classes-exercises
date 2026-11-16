# `002` The `__init__` and `__str__` Methods

Methods with names like `__method__` are called **special methods** (or "magic methods"). Python calls them automatically:

+ `__init__` runs when you create a new instance and sets its initial attributes.
+ `__str__` runs when you `print()` an object or call `str()` on it, and returns a human-friendly text.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"


person1 = Person("Juan", 25)
print(person1)  # Juan, 25 years old
```

## 📝 Instructions:

1. Create a class called `Book` whose `__init__` stores `title`, `author` and `year`.

2. Add a `__str__` method that **returns** the book's information in three lines, exactly like the example.

## 📎 Example:

```py
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book1)
# Book Title: The Great Gatsby
# Author: F. Scott Fitzgerald
# Year: 1925
```

## 💡 Hints:

+ Use `\n` inside a string to create a line break.

+ `__str__` must **return** the text, not print it.
