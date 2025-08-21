import os
from multiprocessing.connection import Connection

from dotenv import load_dotenv, dotenv_values
load_dotenv()

from pymongo import MongoClient ,errors

class FetchData:
    def __init__(self):
        self.user = os.getenv("user")
        self.password = os.getenv("pass")
        self.DBname = os.getenv("DBname")
        self.collection = os.getenv("collectionName")
        self.conn = None
    def connect(self):
        try:
            self.conn = MongoClient(f"mongodb+srv://{self.user}:{self.password}"
                               f"@{self.DBname}.gurutam.mongodb.net/")
            self.conn.server_info()
            #print("MongoDB connected successfully")
            return self.conn
        except errors.ServerSelectionTimeoutError as e:
            print("Failed to connect to MongoDB:", e)
            return None
        except errors.OperationFailure as e:
            print("Authentication failed:", e)
            return None

    def fetch(self):
        self.connect()
        if self.conn:
            db = self.conn[f"{self.DBname}"]
            collection = db[f"{self.collection}"]
            return collection
        else:
            return "connection did not created"
if __name__ == '__main__':

    a = FetchData()
    for i in a.fetch().find().limit(3):
        print(i)