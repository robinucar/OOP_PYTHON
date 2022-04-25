class Person:
    number_of_people = 0 #class attribute

    def __init__(self,name):
        self.name = name
        Person.add_person()
        

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('Robin')
p2 = Person('Alex')
print(Person.get_number_of_people()) #2
