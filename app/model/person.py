class Person:

    def __init__(self, name, age = 0, email = ""):
        self.name = name
        self.age = age
        self.email = email

    def __eq__(self, other) :
        return self.__dict__ == other.__dict__
