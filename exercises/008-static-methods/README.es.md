# `008` Métodos estáticos

Un **método estático** pertenece a una clase pero no recibe `self` ni la clase: es una función normal agrupada dentro de la clase porque está relacionada con ella. Se define con el decorador `@staticmethod` y normalmente se llama sobre la propia clase.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18


print(Person.is_adult(25))  # True
print(Person.is_adult(16))  # False
```

## 📝 Instrucciones:

1. Crea una clase llamada `MathOperations`.

2. Añade un método estático `add_numbers(a, b)` que **retorne** la suma de ambos números.

3. Añade un método estático `is_even(number)` que **retorne** `True` si el número es par y `False` en caso contrario.

4. Llama a ambos métodos directamente sobre la clase (sin crear una instancia) e imprime los resultados.

## 📎 Ejemplo:

```py
print(MathOperations.add_numbers(10, 15))  # 25
print(MathOperations.is_even(7))  # False
```

## 💡 Pista:

+ Escribe `@staticmethod` en la línea justo encima de la definición de cada método.
