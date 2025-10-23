import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracted detailed error information including file name, line numner and the error message. 

    :param error: the exception that occured
    :param error_details: the sys module to access traceback details 
    :return: a formatted error message string 
    """
    # extracted traceback details (exception information )
    _, _, exc_tb = error_detail.exc_info()

    # get the file name wherein the error occured 
    filename = exc_tb.tb_frame.f_code.co_filename

    # create a formatted error message string with file name, line number, and the actual error 
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script: {filename} at line number [{line_number}]: {str(error)}"

    # log the error for better tracking 
    logging.error(error_message)

    return error_message

class MyException(Exception):
    """
    Custom exception class for handling errors
    """
    def __init__(self, error_message: str, error_detail: sys):
        # call the base class constructor with error message 
        super().__init__(error_message)

        # format the detailed error message using error_message_detail function 
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message
        """
        return self.error_message