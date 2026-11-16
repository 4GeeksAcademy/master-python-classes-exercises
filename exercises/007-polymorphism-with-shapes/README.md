# `007` Polymorphism with Shapes

**Polymorphism** means that different classes can respond to the same method in their own way. Code that uses those objects doesn't need to know which class each one is: it just calls the method.

```py
for shape in [Rectangle(2, 3), Circle(1)]:
    print(shape.area())  # Each shape calculates its own area
```

## 📝 Instructions:

1. In `app.py` you have a base class `Shape` whose `area()` method raises an error. Don't modify it.

2. Create a class `Rectangle(Shape)` that stores `width` and `height` and overrides `area()` to **return** `width * height`.

3. Create a class `Circle(Shape)` that stores `radius` and overrides `area()` to **return** `math.pi * radius ** 2`.

4. Create a function `total_area(shapes)` that receives a list of shapes and **returns** the sum of their areas, rounded to 2 decimals.

## 📎 Example:

```py
shapes = [Rectangle(2, 3), Circle(1), Rectangle(1, 1)]
print(total_area(shapes))  # 10.14
```

## 💡 Hint:

+ `total_area` doesn't need any `if`: just call `shape.area()` for every shape.
