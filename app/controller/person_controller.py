from pymongo import MongoClient

class PersonController:
    def __init__(self):
        self.mongo_client = MongoClient()
