# `004` Atributos de clase

Los atributos creados con `self.` dentro de `__init__` pertenecen a **cada instancia**. Los atributos definidos directamente en el cuerpo de la clase pertenecen a la **clase** y los comparten todas las instancias:

```py
class Bicycle:
    wheels = 2  # Class attribute: shared by all bicycles

    def __init__(self, color):
        self.color = color  # Instance attribute: different for each bicycle


print(Bicycle.wheels)  # 2
print(Bicycle("red").wheels)  # 2
```

## 📝 Instrucciones:

1. Crea una clase llamada `Car` con un **atributo de clase** `wheels` igual a `4`.

2. Su `__init__` recibe y guarda los atributos de instancia `brand` y `model`.

3. Añade un método `description()` que **retorne** `"<brand> <model> with <wheels> wheels"`, leyendo `wheels` del atributo de clase.

## 📎 Ejemplo:

```py
car = Car("Toyota", "Corolla")
print(car.description())  # Toyota Corolla with 4 wheels
print(Car.wheels)  # 4
```

## 💡 Pista:

+ Dentro de un método puedes leer un atributo de clase con `self.wheels` o `Car.wheels`.
