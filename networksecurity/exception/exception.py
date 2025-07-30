import sys
from networksecurity.logging.logger import logger
# ...existing code...

class NetworkSecurityException(Exception):
    """Base class for all exceptions in the Network Security System."""
    def __init__(self, error_message, error_details):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in script: [{self.file_name}] at line number: "
            f"[{self.line_number}] with error message: [{self.error_message}]"
        )

if __name__ == "__main__":
    try:
        logger.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed")
    except Exception as e:
        print("An exception occurred")