# modules/base_module.py
# Version: 1.0.1

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseModule(ABC):
    def __init__(self, logger):
        self.logger = logger

    @abstractmethod
    def collect_data(self, base_path: str) -> Dict[str, Any]:
        pass

    def log(self, message: str, level: str = 'info'):
        """Log messages to both terminal and file"""
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        else:
            self.logger.info(message)
