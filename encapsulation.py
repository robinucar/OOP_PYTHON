class Person:
    def __init__(self, name, age, nationality, gender):
        self.__name = name
        self.__age = age
        self.__nationality = nationality
        self.__gender = gender

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
         self.__name = value
    
p = Person('Robin', 34, 'British', 'Male')
# print(p.__age) #Output: AttributeError: 'Person' object has no attribute '__age'  - double _ make variable private
print(p.get_name())
p.set_name('Melsa')
print(p.get_name())