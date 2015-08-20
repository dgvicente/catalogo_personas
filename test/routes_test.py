from nose.tools import *
from app.person import Person
from helpers.helpers import *

class TestRoutes:

    def test_should_have_name_of_the_person(self):
        expected_name = random_word(10)
        person = Person(expected_name)
        actual_name = person.name
        assert_equal(expected_name, actual_name)

    def test_should_have_the_age_of_the_person(self):
        expected_age = 25
        person = Person('Pepe', expected_age)
        actual_age = person.age
        assert_equal(expected_age, actual_age)

    def test_age_should_be_zero_when_age_is_not_given(self):
        person = Person('Pepe')
        assert_equal(0, person.age)

    def test_should_have_the_email_of_the_person(self):
        expected_email = 'dianagv@gmail.com'
        person = Person('Pepe', email=expected_email)
        actual_email = person.email
        assert_equal(expected_email, actual_email)

    def test_email_should_not_be_mandatory(self):
        person = Person('Pepe')
        assert_equal("", person.email)
