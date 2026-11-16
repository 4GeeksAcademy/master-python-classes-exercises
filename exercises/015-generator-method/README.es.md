# `015` Una clase con un generador

Un **generador** es una función que usa `yield` en lugar de `return`. Cada `yield` produce un valor y pausa la función hasta que se pide el siguiente. Así, los valores se generan de uno en uno en lugar de construir una lista completa en memoria.

```py
def count_up_to(n):
    for number in range(1, n + 1):
        yield number


print(list(count_up_to(3)))  # [1, 2, 3]
```

## 📝 Instrucciones:

1. Crea una clase `DivisibleBySeven` cuyo `__init__` guarde un número `n`.

2. Añade un método generador `generate()` que produzca con **`yield`**, uno a uno, todos los números entre `0` y `n` (ambos incluidos) que sean divisibles entre `7`.

## 📎 Ejemplo:

```py
numbers = DivisibleBySeven(30)
for number in numbers.generate():
    print(number)  # 0, 7, 14, 21, 28 (one per line)

print(list(DivisibleBySeven(14).generate()))  # [0, 7, 14]
```

## 💡 Pista:

+ Debes usar `yield` en tu solución: no construyas ni retornes una lista.
