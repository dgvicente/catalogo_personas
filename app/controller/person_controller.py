from pymongo import MongoClient
import json

class PersonController:

    def __init__(self):
        self.mongo_client = MongoClient()
        self.database = self.mongo_client.catalogo_personas

    def insert(self, person):
        persons_collection = self.database['persons']
        return persons_collection.insert_one(person.__dict__).inserted_id
