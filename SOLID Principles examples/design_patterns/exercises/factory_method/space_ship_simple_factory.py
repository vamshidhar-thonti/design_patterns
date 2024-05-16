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
    
class SpaceShipFactory:
    @staticmethod
    def create_space_ship(context):
        if context.space_ship_type == SpaceShipType.MILLENIUM_FALCON:
            return MilleniumFalcon(context.data)
        elif context.space_ship_type == SpaceShipType.UNSC_INFINITY:
            return UNSCInfinity(context.data)
        elif context.space_ship_type == SpaceShipType.USS_ENTERPRISE:
            return USSEnterprise(context.data)
        elif context.space_ship_type == SpaceShipType.SERENITY:
            return Serenity(context.data)
        else:
            raise ValueError('Invalid Space Ship type')
        
class SpaceShipContext:
    def __init__(self, space_ship_type, data) -> None:
        self.space_ship_type = space_ship_type
        self.data = data

def main():
    millenium_falcon_data = {
        'displayName': 'Millenium Falcon',
        'size': (100, 200),
        'position': (12.23, 23.5),
        'speed': 1234
    }
    millenium_falcon_context = SpaceShipContext(SpaceShipType.MILLENIUM_FALCON, millenium_falcon_data)
    millenium_falcon = SpaceShipFactory.create_space_ship(millenium_falcon_context)
    print(millenium_falcon.get_info())

if __name__ == '__main__':
    main()
