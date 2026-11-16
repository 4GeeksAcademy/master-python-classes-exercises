# `005` Los métodos `__repr__` y `__eq__`

Por defecto, dos objetos distintos nunca son iguales, aunque tengan los mismos datos, y al imprimirlos se ve algo como `<__main__.Point object at 0x7f...>`. Dos métodos especiales lo solucionan:

+ `__repr__` retorna un texto para desarrolladores, normalmente mostrando cómo recrear el objeto. Se usa en la consola y dentro de listas.
+ `__eq__(self, other)` define cuándo dos objetos son iguales con `==`.

## 📝 Instrucciones:

1. Crea una clase llamada `Point` cuyo `__init__` guarde `x` e `y`.

2. Añade un método `__repr__` que **retorne** `"Point(<x>, <y>)"`.

3. Añade un método `__eq__` que **retorne** `True` cuando el otro objeto también sea un `Point` con los mismos `x` e `y`, y `False` en caso contrario.

## 📎 Ejemplo:

```py
a = Point(1, 2)
b = Point(1, 2)
print(a)  # Point(1, 2)
print([a, Point(0, 0)])  # [Point(1, 2), Point(0, 0)]
print(a == b)  # True
print(a == Point(2, 1))  # False
print(a == "Point(1, 2)")  # False
```

## 💡 Pista:

+ `isinstance(other, Point)` comprueba si `other` es un `Point`.
