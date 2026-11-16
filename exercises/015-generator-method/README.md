# `015` A Class with a Generator

A **generator** is a function that uses `yield` instead of `return`. Each `yield` produces one value and pauses the function until the next value is requested. That way, values are generated one at a time instead of building a whole list in memory.

```py
def count_up_to(n):
    for number in range(1, n + 1):
        yield number


print(list(count_up_to(3)))  # [1, 2, 3]
```

## 📝 Instructions:

1. Create a class `DivisibleBySeven` whose `__init__` stores a number `n`.

2. Add a generator method `generate()` that **yields**, one by one, every number between `0` and `n` (both included) that is divisible by `7`.

## 📎 Example:

```py
numbers = DivisibleBySeven(30)
for number in numbers.generate():
    print(number)  # 0, 7, 14, 21, 28 (one per line)

print(list(DivisibleBySeven(14).generate()))  # [0, 7, 14]
```

## 💡 Hint:

+ You must use `yield` in your solution: don't build and return a list.
