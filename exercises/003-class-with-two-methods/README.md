# `003` Class with Two Methods

Objects keep their state between method calls: one method can save a value in an attribute and another method can use it later.

## 📝 Instructions:

1. Create a class called `TextFormatter`. Its `__init__` doesn't receive parameters and sets the attribute `text` to an empty string.

2. Add a method `set_text(text)` that saves the received text in the attribute `text`.

3. Add a method `get_uppercase()` that **returns** the saved text in uppercase.

## 📎 Example:

```py
formatter = TextFormatter()
formatter.set_text("hello world")
print(formatter.get_uppercase())  # HELLO WORLD
```

## 💡 Hint:

+ Inside `set_text`, `self.text = text` saves the parameter in the object.
