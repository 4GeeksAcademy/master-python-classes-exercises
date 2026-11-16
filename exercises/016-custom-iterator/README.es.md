# `016` Un iterador personalizado

Un bucle `for` funciona con cualquier objeto que siga el **protocolo de iteración**:

+ `__iter__(self)` retorna el iterador (normalmente `self`).
+ `__next__(self)` retorna el siguiente valor, o lanza `StopIteration` cuando ya no hay más valores.

Implementar ambos métodos permite que tus propios objetos funcionen en bucles `for`, con `list()`, `sum()` y más.

## 📝 Instrucciones:

1. Crea una clase `Countdown` cuyo `__init__` reciba un entero positivo `start`.

2. Implementa `__iter__` y `__next__` para que al recorrer un `Countdown` se produzcan los números desde `start` hasta `1`.

3. Cuando la cuenta atrás llegue al final, `__next__` debe lanzar `StopIteration`.

## 📎 Ejemplo:

```py
for number in Countdown(3):
    print(number)  # 3, 2, 1 (one per line)

print(list(Countdown(5)))  # [5, 4, 3, 2, 1]
```

## 💡 Pista:

+ Guarda el valor actual en un atributo (por ejemplo `self.current`) y disminúyelo en cada llamada a `__next__`.
