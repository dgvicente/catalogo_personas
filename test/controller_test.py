from nose.tools import *
from pymongo import MongoClient
from app.controller.person_controller import PersonController


class TestController:

    def test_mongo_client_shoul_be_sucessfully_created(self):
        client = MongoClient()
        assert client != None

    def test_person_controller_should_have_a_mongo_client_initialized(self):
        person_controller = PersonController()
        assert person_controller.mongo_client != None
