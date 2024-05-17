from abc import ABC, abstractmethod

class Sandwich:
    def __init__(self) -> None:
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def display(self):
        print("Sandwich with the following ingredients: ")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

class SandwichBuilder(ABC):
    def __init__(self) -> None:
        self.sandwich = None

    def create_new_sandwich(self):
        self.sandwich = Sandwich()

    def get_result(self):
        return self.sandwich
    
    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_filling(self):
        return self.sandwich
    
class VegSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredient('Wheat Bread')

    def add_filling(self):
        self.sandwich.add_ingredient("Lettuce")
        self.sandwich.add_ingredient("Paneer Patte")
        self.sandwich.add_ingredient("Cheese Slice")
        self.sandwich.add_ingredient("Mayonnaise")
        self.sandwich.add_ingredient("Onions")

class ChickenSandwichBuidler(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredient("White Bread")

    def add_filling(self):
        self.sandwich.add_ingredient("Lettuce")
        self.sandwich.add_ingredient("Crispy Chicken")
        self.sandwich.add_ingredient("Cheese")
        self.sandwich.add_ingredient("Mayonnaise")

class SandwichDirector:
    def __init__(self, builder: SandwichBuilder) -> None:
        self.builder = builder

    def build_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_result()
    
def main():
    paneer_sandwich_builder = VegSandwichBuilder()
    director = SandwichDirector(paneer_sandwich_builder)
    paneer_sandwich = director.build_sandwich()
    paneer_sandwich.display()

    chicken_sandwich_builder = ChickenSandwichBuidler()
    director.builder = chicken_sandwich_builder
    chicken_sandwich = director.build_sandwich()
    chicken_sandwich.display()

if __name__ == "__main__":
    main()

