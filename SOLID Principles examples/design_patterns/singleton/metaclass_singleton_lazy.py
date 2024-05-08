class SingletonMeta(type):
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance

        return cls._instances[cls]
    
class LazySingleton(metaclass=SingletonMeta):
    def some_method(self):
        # Implement actual logic here
        pass


singleton = LazySingleton()
singleton2 = LazySingleton()

print(singleton is singleton2)