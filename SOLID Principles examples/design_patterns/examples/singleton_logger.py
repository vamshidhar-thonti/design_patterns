from abc import ABC, ABCMeta, abstractmethod
import threading
import logging
import sys

class SingletonMeta(metaclass=ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
        
class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass

class Logger(BaseLogger):
    def __init__(self):
        print('Initializing Logger...')
        self._logger = logging.getLogger('app_logger')
        self._logger.setLevel(logging.DEBUG)
        
        try:
            file_handler = logging.FileHandler(
                './SOLID Principles examples/design_patterns/examples/logs/application.log'
            )
        except Exception as ex:
            print("Works only if executed from the parent folder of all folders")
            sys.exit(1)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)

logger = Logger()
logger.debug('This is a DEBUG message')
logger.info('This is a INFO message')
logger.warning('This is a WARNING message')
logger.error('This is a ERROR message')
logger.critical('This is a CRITICAL message')