import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]
        
class Singleton(metaclass=SingletonMeta):
    pass

def get_singleton_instance():
    s = Singleton()
    print(s)

threads = []

for i in range(10):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()