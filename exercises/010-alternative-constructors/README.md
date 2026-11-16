# `010` Alternative Constructors

A very common use of `@classmethod` is to create **alternative constructors**: methods that create an instance from data in a different format. They end with `return cls(...)`.

```py
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, text):
        day, month, year = text.split("/")
        return cls(int(day), int(month), int(year))


date = Date.from_string("16/11/2026")
print(date.year)  # 2026
```

## 📝 Instructions:

1. Create a class `Person` whose `__init__` stores `name` and `age`.

2. Add a class method `from_string(text)` that receives a string like `"Ana,25"` and **returns** a new `Person` (the age must be an `int`).

3. Add a class method `from_birth_year(name, birth_year, current_year)` that **returns** a new `Person` whose age is `current_year - birth_year`.

## 📎 Example:

```py
ana = Person.from_string("Ana,25")
print(ana.name, ana.age)  # Ana 25

leo = Person.from_birth_year("Leo", 2000, 2026)
print(leo.name, leo.age)  # Leo 26
```

## 💡 Hint:

+ Use `cls(...)` instead of `Person(...)`: that way the method also works for child classes.
