from typing import Tuple, List
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

class WeatherData(Subject):
    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def set_measurements(self, temperature, humidity, pressure) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.notify()

    def get_measurements(self) -> Tuple:
        return (self._temperature, self._humidity, self._pressure)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

################### Observers ###################
class CurrentConditionsDisplay(Observer):
    def update(self, subject: WeatherData):
        temperature, humidity, pressure = subject.get_measurements()
        print(f"The current weather is as follows: Tempearture={temperature}, Humidity={humidity}, Pressure={pressure}")

class StatisticsConditionsDisplay(Observer):
    def update(self, subject: WeatherData):
        temperature, humidity, pressure = subject.get_measurements()
        print(f"The statistics weather is as follows: Tempearture={temperature}, Humidity={humidity}, Pressure={pressure}")

class ForecastConditionsDisplay(Observer):
    def update(self, subject: WeatherData):
        temperature, humidity, pressure = subject.get_measurements()
        print(f"The forecast weather is as follows: Tempearture={temperature}, Humidity={humidity}, Pressure={pressure}")


def main():
    publisher = WeatherData()

    observers = [
        CurrentConditionsDisplay(),
        StatisticsConditionsDisplay(),
        ForecastConditionsDisplay()
    ]

    for observer in observers:
        publisher.attach(observer)

    publisher.set_measurements(20.0, 2.3, 2.0)

    publisher.detach(observers[0])

    publisher.set_measurements(10.0, 2.3, 2.0)

if __name__ == "__main__":
    main()