class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        if cls not in cls._instances:
            super().__init__(name, bases, dct)
            # print("initializing <super>...")
            print('1')
            cls._instances[cls] = super().__call__()
            print('3')
    
    def __call__(cls, *args, **kwargs):
        print('In call')
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print('2')
        # print("initializing <child>...")
        self.attribute = "I am Singleton"

# singleton_1 = Singleton()
# singleton_2 = Singleton()

# print(singleton_1 is singleton_2)
