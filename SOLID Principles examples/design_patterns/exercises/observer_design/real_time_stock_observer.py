from typing import List, Tuple

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
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

class Stock(Subject):
    def __init__(self, exchange, symbol, price) -> None:
        self._observers: List[Observer] = []
        self._exchange: str = exchange
        self._symbol: str = symbol
        self._price: float = price
        self._delta_price: float = 0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def set_price(self, new_price: float) -> None:
        self._delta_price = new_price - self._price
        self._price = new_price

        self.notify(self._exchange)

    def get_price(self) -> Tuple:
        return (self._exchange, self._symbol, self._price, self._delta_price)

    def notify(self, exchange) -> None:
        for observer in self._observers:
            if observer.name == exchange:
                observer.update(self)
            else:
                observer.update(self)

class BSEStockObserver(Observer):
    def __init__(self) -> None:
        self.name = "BSE"
    
    def update(self, subject: Stock):
        exchange, symbol, price, delta_price = subject.get_price()
        print(f"The {exchange} stock {symbol} price is updated to {price} with a difference of {delta_price}")

class NSEStockObserver(Observer):
    def __init__(self) -> None:
        self.name = "NSE"
    
    def update(self, subject: Stock):
        exchange, symbol, price, delta_price = subject.get_price()
        print(f"The {exchange} stock {symbol} price is updated to {price} with a difference of {delta_price}")

def main():
    irctc_bse = Stock("BSE", "IRCTC", 890)
    irctc_nse = Stock("NSE", "IRCTC", 890)
    zomato_bse = Stock("BSE", "ZOMATO", 120)
    zomato_nse = Stock("NSE", "ZOMATO", 120)

    bse_stock_observer = BSEStockObserver()
    nse_stock_observer = NSEStockObserver()

    irctc_bse.attach(bse_stock_observer)
    irctc_nse.attach(nse_stock_observer)
    zomato_bse.attach(bse_stock_observer)
    zomato_nse.attach(nse_stock_observer)

    irctc_bse.set_price(900)
    zomato_nse.set_price(100)
    irctc_nse.set_price(90)
    zomato_bse.set_price(1000)

if __name__ == "__main__":
    main()