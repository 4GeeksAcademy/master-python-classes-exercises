class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(MathOperations.add_numbers(10, 15))
print(MathOperations.is_even(7))
