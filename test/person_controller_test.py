from nose.tools import *
from pymongo import MongoClient
from app.controller.person_controller import PersonController
from app.model.person import Person
import json


class TestPersonController:

    def setUp(self):
        self.person_controller = PersonController()
        self.client = MongoClient()
        self.database = self.client.catalogo_personas
        self.person = Person("Diana", 32, "dianagv@gmail.com")

    def tearDown(self):
        self.database['persons'].remove(self.person.__dict__)

    def test_mongo_client_should_be_sucessfully_created(self):
        assert self.client != None

    def test_should_have_a_mongo_client_initialized(self):
        assert self.person_controller.mongo_client != None

    def test_should_have_a_database_initialized(self):
        database = self.person_controller.database
        assert database != None

    def test_should_have_an_insert_method(self):
        inserted_id = self.person_controller.insert(self.person)
        assert inserted_id != None

    def test_should_insert_a_person_and_return_inserted_id(self):
        inserted_id = self.person_controller.insert(self.person)
        expected_id = self.database['persons'].find_one(self.person.__dict__)['_id']
        assert_equal(inserted_id, expected_id)

    def test_should_have_an_list_all_method(self):
        person_list = self.person_controller.list_all()
        assert person_list != None

    def test_should_list_all_inserted_persons(self):
        self.person_controller.insert(self.person)
        person_list = self.person_controller.list_all()
        assert len(person_list) > 0
        assert_equal(person_list[0].name, self.person.name)
