# from src.logger import logging

# logging.debug("This is a debug")
# logging.info("This is a info")
# logging.warning("This is a warning")
# logging.error("This is a error")
# logging.critical("This is a critical")

# ________________

# # below code is for exception handling 
# from src.logger import logging
# from src.exception import MyException
# import sys
# try:
#     a = 1+"Z"
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e 

# for data ingestion pipeline 
from src.pipline.training_pipeline import TrainPipeline
pipeline = TrainPipeline()
pipeline.run_pipeline()