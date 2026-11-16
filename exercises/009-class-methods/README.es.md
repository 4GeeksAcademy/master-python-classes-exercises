# `009` Métodos de clase

Un **método de clase** recibe la propia clase como primer parámetro, normalmente llamado `cls`, en lugar de una instancia. Se define con `@classmethod` y puede leer o cambiar **atributos de clase**.

```py
class Person:
    total_people = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        Person.total_people += 1

    @classmethod
    def get_total_people(cls):
        return cls.total_people


Person("Alice")
Person("Bob")
print(Person.get_total_people())  # 2
```

## 📝 Instrucciones:

1. Crea una clase llamada `CircleCalculator` con un atributo de clase `pi` igual a `3.14159`.

2. Añade un método de clase `calculate_area(radius)` que **retorne** `pi * radius ** 2`, leyendo `pi` a través de `cls`.

3. Llama al método sobre la clase, sin crear una instancia, e imprime el resultado.

## 📎 Ejemplo:

```py
print(CircleCalculator.calculate_area(5))  # 78.53975
```

## 💡 Pistas:

+ Escribe `@classmethod` encima del método y usa `cls` como su primer parámetro.

+ Compáralo con el ejercicio anterior: un método estático no recibe `cls`, así que no puede usar los atributos de clase de forma flexible.
