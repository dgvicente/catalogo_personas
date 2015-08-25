from pymongo import MongoClient
from app.model.person import Person
import json

class PersonController:

    def __init__(self):
        self.mongo_client = MongoClient()
        self.database = self.mongo_client.catalogo_personas

    def insert(self, person):
        persons_collection = self.database['persons']
        return persons_collection.insert_one(person.__dict__).inserted_id

    def list_all(self):
        return [Person(**self._remove_id(p)) for p in list(self.database['persons'].find())]

    def _remove_id(self, elem):
        elem.pop('_id')
        return elem
