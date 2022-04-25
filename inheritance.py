# General class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

# Spesific Class
class Cat(Pet):
    def speak(Self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print('Bark')

p = Pet('Tim', 19)
p.show() # I am Tim and I am 19 years old.
c = Cat('Milly', 4)
c.show() # inherited show method from Upper class which is Pet Output: I am Milly and I am 4 years old.
d = Dog('Jill', 5)
d.show() # inherited show method from Upper class which is Pet Output: I am Jill and I am 5 years old.