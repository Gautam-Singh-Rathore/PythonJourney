# Inheritance

class Mamal:
    def walk(self):
        print("I am walking")

class Dog(Mamal) :
    pass

class Cat(Mamal):
    pass

lawania = Dog()
lawania.walk()

