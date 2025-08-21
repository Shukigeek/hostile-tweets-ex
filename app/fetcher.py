import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from pymongo import MongoClient ,errors

class FetchData:
    def __init__(self):
        self.user = os.getenv("user")
        self.password = os.getenv("pass")
        self.DB_name = os.getenv("DBname")
        self.collection = os.getenv("collectionName")
        self.conn = None
    def connect(self):
        try:
            self.conn = MongoClient(f"mongodb+srv://{self.user}:{self.password}"
                               f"@{self.DB_name}.gurutam.mongodb.net/")
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
            db = self.conn[f"{self.DB_name}"]
            collection = db[f"{self.collection}"]
            return collection.find({},{"_id":0}).to_list()
        else:
            return "connection did not created"
if __name__ == '__main__':

    a = FetchData()
    for i in a.fetch().find({"_id":0}).limit(3):
        print(i)