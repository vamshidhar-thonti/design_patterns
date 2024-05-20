from abc import ABC, abstractmethod

class Shipping(ABC):
    @abstractmethod
    def calculate_shipping_cost(self, weight) -> float:
        pass

class FedExShipping(Shipping):
    def calculate_shipping_cost(self, weight) -> float:
        return weight * 2.5

class UPSShipping(Shipping):
    def calculate_shipping_cost(self, weight) -> float:
        return weight * 3

class DHLShipping(Shipping):
    def calculate_shipping_cost(self, weight) -> float:
        return weight * 4

class AmazonShipping(Shipping):
    def calculate_shipping_cost(self, weight) -> float:
        return weight * 3.25

class ShippingCostCalculator:
    def __init__(self, carrier: Shipping) -> None:
        self.carrier = carrier

    def calculate(self, weight) -> float:
        return self.carrier.calculate_shipping_cost(weight)

print("Select a carrier for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")
print("4. Amazon")

choice = int(input("Enter the number corresponding to your choice: "))
weight = float(input("Enter the weight of the package (in pounds): "))

if choice == 1:
    carrier = FedExShipping()
elif choice == 2:
    carrier = UPSShipping()
elif choice == 3:
    carrier = DHLShipping()
elif choice == 4:
    carrier = AmazonShipping()
else:
    print("Invalid choice!")
    exit(1)

shipping_cost_instance = ShippingCostCalculator(carrier)
shipping_cost = shipping_cost_instance.calculate(weight)
print(f"The shipping cost for {carrier.__class__.__name__} is ${shipping_cost:.2f}")