import threading

class SingletonLazyMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__()
                cls._instances[cls] = instance
            
        return cls._instances[cls]
        
class SequenceGenerator(metaclass=SingletonLazyMeta):
    def __init__(self) -> None:
        self.number = 0
        print(self.number)

    def get_next_number(self):
        self.number += 1
        return self.number
    
def get_sequence_generator_instance():
    s = SequenceGenerator()
    print(s.get_next_number())

# for i in range(100):
#     get_sequence_generator_instance()

################### Eager Loading ###################

class SingletonEagerMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        print(new_class)
        new_class_instance = super(SingletonEagerMeta, new_class).__call__()
        print(new_class_instance)
        cls._instances[new_class] = new_class_instance
        return new_class
    
    def __call__(cls, *args, **kwargs):
        # print("Metaclass __call__ called", cls._instances[cls])
        return cls._instances[cls]

class SequenceGeneratorEager(metaclass=SingletonEagerMeta):
    def __init__(self) -> None:
        self.number = 0

    def get_next_number(self):
        self.number += 1
        print(self.number)

def get_eager_sequence_generator():
    s = SequenceGeneratorEager()
    s.get_next_number()

for i in range(100):
    get_eager_sequence_generator()