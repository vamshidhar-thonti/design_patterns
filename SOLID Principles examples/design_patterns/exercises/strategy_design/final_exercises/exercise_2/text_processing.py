import sys
from abc import ABC, abstractmethod

class TextTransform(ABC):
    @abstractmethod
    def transform(self, text: str) -> str:
        pass

class UppercaseTextTransform(TextTransform):
    def transform(self, text: str) -> str:
        return text.upper()

class LowercaseTextTransform(TextTransform):
    def transform(self, text: str) -> str:
        return text.lower()

class CapitalizeTextTransform(TextTransform):
    def transform(self, text: str) -> str:
        return text.capitalize()
    
class ProcessText(ABC):
    def __init__(self, transform_type: TextTransform) -> None:
        self._transform_type = transform_type

    @abstractmethod
    def process(self) -> str:
        pass

class CustomProcessText(ProcessText):
    def __init__(self, transform_type: TextTransform) -> None:
        super().__init__(transform_type)

    def process(self, text: str) -> str:
        return self._transform_type.transform(text)


print("########### TEXT TRANSFORM ###########")
print("Choose a Text Transform operation: ")
print("1. Uppercase")
print("2. Lowercase")
print("3. Capitalize")

operation_type = input("Enter a number from the above choices: ")
input_text = input("Enter the text to transformed: ")

if operation_type == "1":
    operation = UppercaseTextTransform()
elif operation_type == "2":
    operation = LowercaseTextTransform()
elif operation_type == "3":
    operation = CapitalizeTextTransform()
else:
    print("Invalid choice")
    sys.exit(1)

instance = CustomProcessText(operation)
output_text = instance.process(input_text)
print(output_text)