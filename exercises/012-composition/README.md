# `012` Composition

Inheritance models an "**is a**" relationship (a `CollegeStudent` *is a* `Student`). **Composition** models a "**has a**" relationship: an object contains other objects as attributes. For example, a library *has* books:

```py
class Library:
    def __init__(self):
        self.books = []  # A Library has a list of Book objects
```

Composition is often simpler and more flexible than inheritance.

## 📝 Instructions:

1. In `app.py` you already have a `Book` class with `title` and `author`.

2. Create a class `Library` whose `__init__` creates an empty list `books`.

3. Add a method `add_book(book)` that appends a `Book` to the list.

4. Add a method `find_by_author(author)` that **returns** a list with the **titles** of the books by that author, in the order they were added.

5. Add a `__len__` method so that `len(library)` **returns** the number of books.

## 📎 Example:

```py
library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Dune", "Frank Herbert"))
library.add_book(Book("Animal Farm", "George Orwell"))

print(len(library))  # 3
print(library.find_by_author("George Orwell"))  # ['1984', 'Animal Farm']
```

## 💡 Hint:

+ `__len__` is another special method: Python calls it when you use `len()` on your object.
