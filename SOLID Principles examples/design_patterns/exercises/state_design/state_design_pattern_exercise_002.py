class TextEditor:
    def __init__(self):
        self.state = DefaultState()
        self.history = []
        self.popped = []
        self.text = ""

    def enter_text(self, text):
        if self.state.__class__.__name__ == "BoldState":
            style = "<bold>{text}<bold/>"
        elif self.state.__class__.__name__ == "ItalicState":
            style = "<italic>{text}<italic/>"
        elif self.state.__class__.__name__ == "UnderlineState":
            style = "<underline>{text}<underline/>"
        else:
            style = "{text}"

        styled_text = style.format(text=text)
        self.history.append(styled_text)
        self.display()

    def apply_bold(self):
        self.state = BoldState()

    def apply_italic(self):
        self.state = ItalicState()

    def apply_underline(self):
        self.state = UnderlineState()

    def undo(self):
        popped_item = self.history.pop(-1)
        self.popped.append(popped_item)
        self.display()

    def redo(self):
        popped_item = self.popped.pop(-1)
        self.history.append(popped_item)
        self.display()

    def display(self):
        print(' '.join(self.history))

class DefaultState:
    def __init__(self):
        pass

class BoldState:
    def __init__(self):
        pass

class ItalicState:
    def __init__(self):
        pass

class UnderlineState:
    def __init__(self):
        pass

text_editor = TextEditor()

running = True
while running:
    print()
    print("Choose from the below options: ")
    print("1. Enter Text")
    print("2. Apply Bold")
    print("3. Apply Italic")
    print("4. Apply Underline")
    print("5. Undo")
    print("6. Redo")
    print("7. Exit")

    option = input("Enter your choice here: ")

    actions = {
        "1": text_editor.enter_text,
        "2": text_editor.apply_bold,
        "3": text_editor.apply_italic,
        "4": text_editor.apply_underline,
        "5": text_editor.undo,
        "6": text_editor.redo,
        "7": False
    }

    if option == "1":
        text = input("Enter text: ")
        actions[option](text)
    elif option == "7":
        running = False
    else:
        actions[option]()