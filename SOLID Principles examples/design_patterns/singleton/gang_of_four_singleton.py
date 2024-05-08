class ClassicSingleton:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("Call get_instance() for ClassicSingleton instance")
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        
        return cls._instance
    
singleton_instance = ClassicSingleton.get_instance()
print(singleton_instance)
singleton_instance = ClassicSingleton.get_instance()
print(singleton_instance)
singleton_instance = ClassicSingleton.get_instance()
print(singleton_instance)
