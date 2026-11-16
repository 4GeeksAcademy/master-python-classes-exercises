# `016` A Custom Iterator

A `for` loop works with any object that follows the **iterator protocol**:

+ `__iter__(self)` returns the iterator (usually `self`).
+ `__next__(self)` returns the next value, or raises `StopIteration` when there are no more values.

Implementing both methods lets your own objects work in `for` loops, `list()`, `sum()` and more.

## 📝 Instructions:

1. Create a class `Countdown` whose `__init__` receives a positive integer `start`.

2. Implement `__iter__` and `__next__` so that iterating a `Countdown` produces the numbers from `start` down to `1`.

3. When the countdown reaches the end, `__next__` must raise `StopIteration`.

## 📎 Example:

```py
for number in Countdown(3):
    print(number)  # 3, 2, 1 (one per line)

print(list(Countdown(5)))  # [5, 4, 3, 2, 1]
```

## 💡 Hint:

+ Keep the current value in an attribute (for example `self.current`) and decrease it in each call to `__next__`.
