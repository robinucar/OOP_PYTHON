# General class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print('I do not know what to say')

# Spesific Class
class Cat(Pet):
    def speak(Self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    pass

p = Pet('Tim', 19)
p.show() # I am Tim and I am 19 years old.
c = Cat('Milly', 4)
c.show() # inherited show method from Upper class which is Pet Output: I am Milly and I am 4 years old.
d = Dog('Jill', 5)
d.show() # inherited show method from Upper class which is Pet Output: I am Jill and I am 5 years old.
f = Fish('Gold', 3) 
f.show() # inherited show method from Upper class which is Pet Output: I am Gold and I am 3 years old.

# Speak
c.speak() # Miyaw   # Cat class speak Method
d.speak() # Bark    # Dog class speak Method
p.speak() # I do not know what to say # Pet class speak method
f.speak() # I do not know what to say # Pet class speak method -Fish class does not have speak method There fore it inherits from upper class Pet

# Overriding is an object-oriented programming feature that enables a child class 
# to provide different implementation for a method that is already defined and/or 
# implemented in its parent class or one of its parent classes.
