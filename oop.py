class Dog:

    def __init__(self, name, age): # initialize
        self.name = name
        self.age = age
    def bark(self):
        print('bark')

    

    def birtdayPassed(self):
        self.age = self.age + 1

    def intro(self):
        return f'Hello, My name is {self.name}. And I am {self.age} years old.'

b = Dog('Boddy', 3)
b.birtdayPassed() # age is 4
b.birtdayPassed() # age is 5 
print(b.intro()) # Hello, My name is Boddy. And I am 5 years old.