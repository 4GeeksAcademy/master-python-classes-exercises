# `006` Herencia y `super()`

Con la **herencia**, una clase hija recibe todos los atributos y métodos de una clase padre, y puede añadir otros nuevos o **sobrescribir** los existentes.

```py
class HighSchoolStudent(Student):  # The parent class goes in parentheses
    def __init__(self, name, age, grade, specialization):
        super().__init__(name, age, grade)  # Reuse the parent's __init__
        self.specialization = specialization

    def study(self, hours):  # Override a parent method
        return f"{self.name} is studying {self.specialization} for {hours} hours."
```

`super()` te da acceso a la clase padre, así no repites su código.

## 📝 Instrucciones:

1. En `app.py` ya tienes una clase `Student`. No la modifiques.

2. Crea una clase `CollegeStudent` que herede de `Student` y añada el atributo `major`. Usa `super()` en su `__init__`.

3. Sobrescribe `introduce()` para que **retorne** `"Hi there! I'm <name>, a college student majoring in <major>."`

4. Añade un nuevo método `attend_lecture()` que **retorne** `"<name> is attending a lecture for <major> students."`

## 📎 Ejemplo:

```py
alice = CollegeStudent("Alice", 20, 90, "Computer Science")
print(alice.introduce())  # Hi there! I'm Alice, a college student majoring in Computer Science.
print(alice.study(3))  # Alice is studying for 3 hours.  (inherited, not changed)
print(alice.attend_lecture())  # Alice is attending a lecture for Computer Science students.
```

## 💡 Pista:

+ Aprende más sobre `super()` en [Real Python: Supercharge Your Classes With Python super()](https://realpython.com/python-super/) (en inglés).
