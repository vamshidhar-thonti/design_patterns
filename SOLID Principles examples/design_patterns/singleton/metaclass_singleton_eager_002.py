class SingletonMeta(type):
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        print("Initializing <super>...")
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instances[new_class] = super(SingletonMeta, new_class).__call__()
        return new_class
    
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self) -> None:
        print("Initializing <child>...")
        self.attribute = "I am Singleton"

singleton_1 = Singleton()
singleton_2 = Singleton()

print(singleton_1 is singleton_2)
