import sys
from logger import logging

def error_message_details(error, error_details:sys):
    '''
    A function to print the error details in a custom way
    '''
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_message = f"""Error in python script {file_name}\n
                        Line number {line_no}\n
                        Error message:\n{str(error)}"""
    return error_message
    

class CustomException(Exception):
    '''
    A custom form of the Exception class to call the error_message_details function  
    '''
    def __init__(self, error, error_details:sys):
        super().__init__(error)
        self.error_message = error_message_details(error, error_details)

    def __str__(self):
        return self.error_message


# test if logging and exception work
# if __name__ == "__main__":

#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("devision by zero")
#         raise CustomException(e, sys)
