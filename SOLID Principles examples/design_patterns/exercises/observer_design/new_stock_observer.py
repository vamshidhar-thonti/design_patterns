from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, product_name: str, new_stock: int) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class StoreManager(Observer):
    def __init__(self, name: str):
        self._name = name

    def update(self, product_name: str, new_stock: int) -> None:
        # TODO: Implement the update method to display a message indicating the stock level update
        print(f"The product {product_name} is below/equal to threshold of 20")


class Inventory(Subject):
    def __init__(self):
        self._observers = []
        self._products = {}

    def attach(self, observer: Observer) -> None:
        # TODO: Implement the attach method to add an observer
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        # TODO: Implement the detach method to remove an observer
        self._observers.remove(observer)

    def notify(self, product_name, new_stock) -> None:
        # TODO: Implement the notify method to notify all observers
        for observer in self._observers:
            observer.update(product_name, new_stock)

    def update_stock(self, product_name: str, new_stock: int) -> None:
        # TODO: Implement the update_stock method to update the stock level and call notify if necessary
        self._products[product_name] = new_stock
        if new_stock < 25:
            self.notify(product_name, new_stock)


if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products to inventory
    inventory._products = {
        "Apples": 10,
        "Oranges": 25,
        "Bananas": 50,
    }
    
    manager1 = StoreManager("Alice")
    manager2 = StoreManager("Bob")
    
    # Attaching store managers
    inventory.attach(manager1)
    inventory.attach(manager2)
    
    # Updating stock levels and checking notifications
    print("Stock level update 1:")
    inventory.update_stock("Apples", 5)  # Should notify both managers
    print("\nStock level update 2:")
    inventory.update_stock("Bananas", 60)  # Should not notify as stock level increased
    
    # Detaching manager1
    inventory.detach(manager1)
    
    # Updating stock levels again
    print("\nStock level update 3:")
    inventory.update_stock("Oranges", 20)  # Should notify only manager2
