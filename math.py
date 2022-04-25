# Static Method

class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def subtract5(x):
        return x - 5

    @staticmethod
    def run():
        print('I am running...')

# No need instance
print(Math.add5(5)) # Output: 10
print(Math.subtract5(10)) #Output: 5
Math.run() #Output: I am running...