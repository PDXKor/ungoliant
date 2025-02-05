import logging
from typing import Optional, Dict, Any

class LoggingMixin:
    """
    A reusable mixin for adding logging capabilities to other classes.
    """
    def __init__(self, logger_name: Optional[str] = None, log_file: Optional[str] = None, log_level: int = logging.INFO):
        """
        Initialize the logger for the class.
        
        :param logger_name: The name of the logger (default: class name).
        :param log_file: Optional file to write logs.
        :param log_level: Logging level.
        """
        logger_name = logger_name or self.__class__.__name__
        self.logger = logging.getLogger(logger_name)

        if not self.logger.hasHandlers():  # Prevent duplicate handlers
            self.logger.setLevel(log_level)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # File handler (if specified)
            if log_file:
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    def log_info(self, message: str):
        """Log an informational message."""
        self.logger.info(message)

    def log_debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)

    def log_warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)

    def log_error(self, message: str):
        """Log an error message."""
        self.logger.error(message)

    def log_exception(self, message: str):
        """Log an exception with traceback."""
        self.logger.exception(message)
