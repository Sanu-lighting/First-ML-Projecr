import sys
import logging
def error_message_details(error , error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename 
    error_messege="Error occuered in the python script named [{0}] line number [{1}] as [{2}]".format(file_name,exc_tb.tb_lineno, str(error))
    return error_messege
class CustomeException(Exception):
    def __init__(self,error_messege , error_detail:sys):
        super().__init__(error_messege)
        self.error_messege=error_message_details(error_messege,error_detail=error_detail)
    def __str__(self):
        return self.error_messege    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Logging has started")
        raise CustomeException(e,sys)

