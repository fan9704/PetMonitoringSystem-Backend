import logging
import sys

from pythonjsonlogger import jsonlogger


class CommandLogger:
    def __init__(self, name: str):
        self.stderr_logger = logging.StreamHandler(sys.stdout)
        self.stderr_logger.setFormatter(jsonlogger.JsonFormatter())
        self.stderr_logger.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger = logging.getLogger(name)
        self.logger.addHandler(self.stderr_logger)

    def getLogger(self):
        return self.logger

    def setLevel(self, logType):
        self.logger.setLevel(logType)
