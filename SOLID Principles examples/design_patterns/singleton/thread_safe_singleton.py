import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)

        return cls._instance
    
s1 = ThreadSafeSingleton()
s2 = ThreadSafeSingleton()

print(s1 is s2)
