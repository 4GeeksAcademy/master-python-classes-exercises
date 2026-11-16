class TextFormatter:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def get_uppercase(self):
        return self.text.upper()


formatter = TextFormatter()
formatter.set_text("hello world")
print(formatter.get_uppercase())
