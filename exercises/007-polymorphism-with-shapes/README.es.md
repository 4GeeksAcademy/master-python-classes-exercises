# `007` Polimorfismo con figuras

**Polimorfismo** significa que clases distintas pueden responder al mismo método a su manera. El código que usa esos objetos no necesita saber de qué clase es cada uno: simplemente llama al método.

```py
for shape in [Rectangle(2, 3), Circle(1)]:
    print(shape.area())  # Each shape calculates its own area
```

## 📝 Instrucciones:

1. En `app.py` tienes una clase base `Shape` cuyo método `area()` lanza un error. No la modifiques.

2. Crea una clase `Rectangle(Shape)` que guarde `width` y `height` y sobrescriba `area()` para **retornar** `width * height`.

3. Crea una clase `Circle(Shape)` que guarde `radius` y sobrescriba `area()` para **retornar** `math.pi * radius ** 2`.

4. Crea una función `total_area(shapes)` que reciba una lista de figuras y **retorne** la suma de sus áreas, redondeada a 2 decimales.

## 📎 Ejemplo:

```py
shapes = [Rectangle(2, 3), Circle(1), Rectangle(1, 1)]
print(total_area(shapes))  # 10.14
```

## 💡 Pista:

+ `total_area` no necesita ningún `if`: solo llama a `shape.area()` en cada figura.
