# `002` Los métodos `__init__` y `__str__`

Los métodos con nombres como `__method__` se llaman **métodos especiales** (o "métodos mágicos"). Python los llama automáticamente:

+ `__init__` se ejecuta al crear una nueva instancia y define sus atributos iniciales.
+ `__str__` se ejecuta cuando haces `print()` de un objeto o llamas a `str()` con él, y retorna un texto legible para personas.

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

## 📝 Instrucciones:

1. Crea una clase llamada `Book` cuyo `__init__` guarde `title`, `author` y `year`.

2. Añade un método `__str__` que **retorne** la información del libro en tres líneas, exactamente como en el ejemplo.

## 📎 Ejemplo:

```py
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book1)
# Book Title: The Great Gatsby
# Author: F. Scott Fitzgerald
# Year: 1925
```

## 💡 Pistas:

+ Usa `\n` dentro de un string para crear un salto de línea.

+ `__str__` debe **retornar** el texto, no imprimirlo.
