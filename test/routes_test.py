from nose.tools import *
from app.person import Person

class TestRoutes:

    def test_should_have_name_of_the_person(self):
        expected_name = 'Diana Garcia'
        person = Person(expected_name)
        actual_name = person.name
        assert_equal(expected_name, actual_name)

    def test_should_have_the_age_of_the_person(self):
        expected_age = 25
        person = Person('Pepe', expected_age)
        actual_age = person.age
        assert_equal(expected_age, actual_age)

    def test_age_should_be_zero_when_not_passed(self):
        person = Person('Pepe')
        assert_equal(0, person.age)