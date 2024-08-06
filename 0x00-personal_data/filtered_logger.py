#!/usr/bin/env python3
"""
filter function
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List,
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(rf'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password"
)
def get_logger() -> logging.Logger:
    """
    returns a logging.Logger object
    """
    # Create a logger named "user_data"
    logger = logging.getLogger("user_data")
    # Only log messages with info level or higher
    logger.setLevel(logging.INFO)
    # Don't send messages to other handlers
    logger.propagate = False
    # Create a console handler to output logs to the console
    handler = logging.StreamHandler()
    # Set the log message format
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    # Add the console handler to the logger
    logger.addHandler(handler)
    return logger
