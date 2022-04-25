class Dog:
    def bark(self):
        print('bark')

    def intro(self, name):
        return f'Hello, My name is {name}'

d = Dog()
d.bark()
print(d.intro('Boddy'))
print(type(d))