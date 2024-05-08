class SimpleSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance
    
    def __init__(self) -> None:
        print("__init__ called")
    
simple_singleton = SimpleSingleton()
print(simple_singleton)
simple_singleton = SimpleSingleton()
print(simple_singleton)
simple_singleton = SimpleSingleton()
print(simple_singleton)