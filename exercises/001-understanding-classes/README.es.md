# `001` Entendiendo las clases

Una **clase** es un plano para crear **objetos**. Cada objeto (o **instancia**) tiene sus propios datos, llamados **atributos**, y puede realizar acciones, llamadas **métodos**.

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

`self` es el propio objeto: `self.name` significa "el nombre de **este** estudiante".

## 📝 Instrucciones:

1. Siguiendo el ejemplo, crea una clase llamada `Pet` cuyo `__init__` reciba y guarde `name`, `species` y `age`.

2. Añade un método `describe()` que **retorne** `"<name> is a <age> year old <species>."`

3. Añade un método `birthday()` que aumente `age` en `1` y **retorne** la nueva edad.

4. Crea una mascota y llama a sus métodos para ver cómo funcionan.

## 📎 Ejemplo:

```py
luna = Pet("Luna", "cat", 3)
print(luna.describe())  # Luna is a 3 year old cat.
print(luna.birthday())  # 4
print(luna.describe())  # Luna is a 4 year old cat.
```

## 💡 Pista:

+ Todo método recibe `self` como primer parámetro, aunque no lo pases al llamar al método.
