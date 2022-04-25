class Person:
    def __init__(self, name, age, nationality, gender):
        self.__name = name
        self.__age = age
        self.__nationality = nationality
        self.__gender = gender


p = Person('Robin', 34, 'British', 'Male')
print(p.__age) #Output: AttributeError: 'Person' object has no attribute '__age'  - double _ make variable private