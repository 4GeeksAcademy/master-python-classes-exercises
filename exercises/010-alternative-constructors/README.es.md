# `010` Constructores alternativos

Un uso muy común de `@classmethod` es crear **constructores alternativos**: métodos que crean una instancia a partir de datos en otro formato. Terminan con `return cls(...)`.

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

## 📝 Instrucciones:

1. Crea una clase `Person` cuyo `__init__` guarde `name` y `age`.

2. Añade un método de clase `from_string(text)` que reciba un string como `"Ana,25"` y **retorne** una nueva `Person` (la edad debe ser un `int`).

3. Añade un método de clase `from_birth_year(name, birth_year, current_year)` que **retorne** una nueva `Person` cuya edad sea `current_year - birth_year`.

## 📎 Ejemplo:

```py
ana = Person.from_string("Ana,25")
print(ana.name, ana.age)  # Ana 25

leo = Person.from_birth_year("Leo", 2000, 2026)
print(leo.name, leo.age)  # Leo 26
```

## 💡 Pista:

+ Usa `cls(...)` en lugar de `Person(...)`: así el método también funciona con las clases hijas.
