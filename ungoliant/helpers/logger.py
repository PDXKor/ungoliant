import logging
from typing import Optional, Dict, Any
import os
from dotenv import load_dotenv
load_dotenv()

class LoggingMixin:
    """
    A reusable mixin for adding logging capabilities to other classes.
    """
    def __init__(
            self,
            logger_name: Optional[str] = None,
            log_file: Optional[str] = None,
            log_level: int = logging.INFO
        ):
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
                formatter = logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )

                # Check env var to see if console logging should be disabled.
                disable_console = os.getenv("DISABLE_CONSOLE_LOGGING", "false").lower() in (
                    "true", "1", "yes"
                )
                if not disable_console:
                    # Console handler
                    console_handler = logging.StreamHandler()
                    console_handler.setFormatter(formatter)
                    self.logger.addHandler(console_handler)
                else:
                    # Optionally, you can log that console logging has been disabled.
                    self.logger.debug("Console logging is disabled via environment variable.")

                # File handler (if specified)
                if log_file:
                    # Check if there is a log dir
                    parent_dir = os.path.dirname(os.path.abspath(__file__))
                    gp_dir = os.path.dirname(parent_dir)
                    logs_dir = os.path.join(gp_dir, 'logs')

                    if not os.path.exists(logs_dir):
                        os.makedirs(logs_dir)

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
