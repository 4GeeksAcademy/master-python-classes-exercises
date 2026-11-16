class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for number in range(self.n + 1):
            if number % 7 == 0:
                yield number


for number in DivisibleBySeven(30).generate():
    print(number)
