import os 
import sys
import pymongo 
import certifi 
from dotenv import load_dotenv
load_dotenv()

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# load certificate aurhority file to acoid timeout errors when connecting to MongoDB 
ca = certifi.where()

class MongoDBClient:
    """
    responsible for eatablishing connection to MongoDB databse
    initializes the mongodb connection using the given db name 
    """
    client = None # shared mongoDB instance across all mongo client instances
    def __init__(self, database_name: str= DATABASE_NAME) -> None:
            # Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.
            #  MyException
            #     If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        try:
            # check if mongoDB connection exists. if not, create new 
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set")
                
                # establish new connection 
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            
            # use the shares mongodb client for this isntance 
            self.client = MongoDBClient.client
            self.database = self.client[database_name] # connect to specifies db
            self.database_name = database_name
            logging.info("MongoDB connection successful ")

        except Exception as e:
            raise MyException(e, sys)