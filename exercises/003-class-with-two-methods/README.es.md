# `003` Clase con dos métodos

Los objetos conservan su estado entre llamadas a métodos: un método puede guardar un valor en un atributo y otro método puede usarlo después.

## 📝 Instrucciones:

1. Crea una clase llamada `TextFormatter`. Su `__init__` no recibe parámetros y asigna un string vacío al atributo `text`.

2. Añade un método `set_text(text)` que guarde el texto recibido en el atributo `text`.

3. Añade un método `get_uppercase()` que **retorne** el texto guardado en mayúsculas.

## 📎 Ejemplo:

```py
formatter = TextFormatter()
formatter.set_text("hello world")
print(formatter.get_uppercase())  # HELLO WORLD
```

## 💡 Pista:

+ Dentro de `set_text`, `self.text = text` guarda el parámetro en el objeto.
