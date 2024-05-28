# utils/logger.py
# Version: 1.0.1

import logging
from logging.handlers import RotatingFileHandler
import os


class Logger:
    def __init__(self, log_file: str):
        """Initialize the logger with console and file handlers"""
        self.logger = logging.getLogger('ProjectDataCollectorLogger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # File handler
        fh = RotatingFileHandler(log_file, maxBytes=5000000, backupCount=5)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def get_logger(self):
        """Get the logger instance"""
        return self.logger
