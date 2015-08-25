from pymongo import MongoClient
from app.model.person import Person
import json

class PersonController:

    def __init__(self):
        self.mongo_client = MongoClient()
        self.database = self.mongo_client.catalogo_personas
        self.persons_collection = self.database['persons']

    def insert(self, person):
        return self.persons_collection.insert_one(person.__dict__).inserted_id

    def list_all(self):
        return [Person(**self._remove_id(p)) for p in list(self.persons_collection.find())]

    def get_by_name(self, name):
        person_dict = self.persons_collection.find_one({"name":name})
        if person_dict:
            return Person(**self._remove_id(person_dict))
        return None

    def _remove_id(self, elem):
        if elem:
            elem.pop('_id')
        return elem
