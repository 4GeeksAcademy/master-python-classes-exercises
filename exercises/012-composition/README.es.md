# `012` Composición

La herencia modela una relación "**es un**" (un `CollegeStudent` *es un* `Student`). La **composición** modela una relación "**tiene un**": un objeto contiene otros objetos como atributos. Por ejemplo, una biblioteca *tiene* libros:

```py
class Library:
    def __init__(self):
        self.books = []  # A Library has a list of Book objects
```

La composición suele ser más simple y flexible que la herencia.

## 📝 Instrucciones:

1. En `app.py` ya tienes una clase `Book` con `title` y `author`.

2. Crea una clase `Library` cuyo `__init__` cree una lista vacía `books`.

3. Añade un método `add_book(book)` que agregue un `Book` a la lista.

4. Añade un método `find_by_author(author)` que **retorne** una lista con los **títulos** de los libros de ese autor, en el orden en que se añadieron.

5. Añade un método `__len__` para que `len(library)` **retorne** la cantidad de libros.

## 📎 Ejemplo:

```py
library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Dune", "Frank Herbert"))
library.add_book(Book("Animal Farm", "George Orwell"))

print(len(library))  # 3
print(library.find_by_author("George Orwell"))  # ['1984', 'Animal Farm']
```

## 💡 Pista:

+ `__len__` es otro método especial: Python lo llama cuando usas `len()` con tu objeto.
