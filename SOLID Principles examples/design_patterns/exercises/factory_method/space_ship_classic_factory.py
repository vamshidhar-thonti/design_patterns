from enum import Enum, auto
from abc import ABC, abstractmethod

class SpaceShipType(Enum):
    MILLENIUM_FALCON = auto()
    UNSC_INFINITY = auto()
    USS_ENTERPRISE = auto()
    SERENITY = auto()

class SpaceShip(ABC):
    def __init__(self, context):
        self.position = context['position']
        self.size = context['size']
        self.displayName = context['displayName']
        self.speed = context['speed']

    @abstractmethod
    def get_info(self):
        pass

class MilleniumFalcon(SpaceShip):
    def __init__(self, context):
        super().__init__(context)

    def get_info(self):
        return f"Name - {self.displayName}\nPosition - {self.position}\nSize - {self.size}\nSpeed - {self.speed}"
    
class UNSCInfinity(SpaceShip):
    def __init__(self, context):
        super().__init__(context)

    def get_info(self):
        return f"Name - {self.displayName}\nPosition - {self.position}\nSize - {self.size}\nSpeed - {self.speed}"
    
class USSEnterprise(SpaceShip):
    def __init__(self, context):
        super().__init__(context)

    def get_info(self):
        return f"Name - {self.displayName}\nPosition - {self.position}\nSize - {self.size}\nSpeed - {self.speed}"
    
class Serenity(SpaceShip):
    def __init__(self, context):
        super().__init__(context)

    def get_info(self):
        return f"Name - {self.displayName}\nPosition - {self.position}\nSize - {self.size}\nSpeed - {self.speed}"
    
class SpaceShipFactory(ABC):
    @abstractmethod
    def create_instance(self, class_name: str, context: dict):
        pass
    
class MilleniumFalconFactory(SpaceShipFactory):
    @staticmethod
    def create_instance(context: dict):
        return MilleniumFalcon(context)

def main():
    millenium_falcon_data = {
        'displayName': 'Millenium Falcon',
        'size': (100, 200),
        'position': (12.23, 23.5),
        'speed': 1234
    }
    millenium_falcon = MilleniumFalconFactory.create_instance(millenium_falcon_data)
    print(millenium_falcon.get_info())

if __name__ == '__main__':
    main()
