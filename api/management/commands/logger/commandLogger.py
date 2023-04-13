import logging
import os
import logstash
import sys
from pythonjsonlogger import jsonlogger


# from logstash_async.handler import AsynchronousLogstashHandler


class CommandLogger:
    def __init__(self, name: str):
        self.stderrLogger = logging.StreamHandler(sys.stdout)
        # self.logstashHandler = logstash.LogstashHandler(
        #     host=os.getenv("LOGSTASH_SERVER_IP", "127.0.0.1"),
        #     port=os.getenv("LOGSTASH_UDP_PORT", 12201),
        #     version=1,
        # )
        # self.logstashHandler.setFormatter(jsonlogger.JsonFormatter())
        self.stderrLogger.setFormatter(jsonlogger.JsonFormatter())
        # self.logstashHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.stderrLogger.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger = logging.getLogger(name)
        # self.logger.addHandler(self.logstashHandler)
        self.logger.addHandler(self.stderrLogger)

    def getLogger(self):
        return self.logger

    def setLevel(self, logType):
        self.logger.setLevel(logType)
