from abc import ABCMeta, abstractmethod
import threading
import logging

class SingletonLazyMeta(ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super(SingletonLazyMeta, cls).__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
# Eager loading doesn't work because the abstract implementation cannot be when the file is loaded.
class SingletonEagerMeta(ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            new_class = super().__new__(cls, *args, **kwargs)
            instance = super(SingletonEagerMeta, new_class).__call__()
            cls._instances[new_class] = instance

            return new_class
            
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]
        
class BaseFileAuditManager(metaclass=SingletonLazyMeta):
    @abstractmethod
    def write(cls, message: str):
        pass
    
class FileAuditManager(BaseFileAuditManager):
    def __init__(self):
        self._logger = logging.getLogger('file_auditor')
        self._logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler('audit.txt')
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
    
    def write(self, message: str):
        self._logger.info(message)

auditor1 = FileAuditManager()
auditor2 = FileAuditManager()

print(auditor1 is auditor2)

auditor1.write("Hello")
auditor2.write("Hello 2")
auditor1.write("Hello 3")
auditor2.write("Hello 4")
