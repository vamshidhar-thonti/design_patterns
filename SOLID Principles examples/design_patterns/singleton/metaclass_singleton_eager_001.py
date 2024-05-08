class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        if cls not in cls._instances:
            super().__init__(name, bases, dct)
            cls._instances[cls] =  super().__call__()
            print("initializing <super>...")
    
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("initializing <child>...")
        self.attribute = "I am Singleton"

singleton_1 = Singleton()
singleton_2 = Singleton()

print(singleton_1 is singleton_2)
