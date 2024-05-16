import threading

class SingletonLazyMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls):
        print('Meta class call')
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__()
                cls._instances[cls] = instance
            
        return cls._instances[cls]
        
class SequenceLazyGenerator(metaclass=SingletonLazyMeta):
    def __init__(self) -> None:
        print('In sub class init')
        self.number = 0
        print(self.number)

    def get_next_number(self):
        self.number += 1
        return self.number
    
def get_sequence_generator_instance():
    s = SequenceLazyGenerator()
    print(s.get_next_number())

# get_sequence_generator_instance()

# for i in range(100):
#     get_sequence_generator_instance()

################### Eager Loading ###################

class SingletonEagerMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            new_class = super().__new__(cls, *args, **kwargs)
            # print(new_class)
            new_class_instance = super(SingletonEagerMeta, new_class).__call__()
            # print(new_class_instance)
            cls._instances[new_class] = new_class_instance
        return new_class
    
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class SequenceGeneratorEager(metaclass=SingletonEagerMeta):
    def __init__(self) -> None:
        self.number = 0

    def get_next_number(self):
        self.number += 1
        print(self.number)

def get_eager_sequence_generator():
    with threading.Lock():
        s = SequenceGeneratorEager()
        s.get_next_number()

threads = []
for i in range(100):
    t = threading.Thread(target=get_eager_sequence_generator)
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()