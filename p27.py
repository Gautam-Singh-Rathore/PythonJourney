# Classes
from HelloWorld.p18 import names


class Point:
    # Constructor
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y=20
# point1.draw()
# print(point1.x)
#
# point2 = Point()
# point2.move()

# Constructor
point3 = Point(10,20)
point3.x = 11
print(point3.x)

# Exercise
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi ! I am {self.name}")

hardik = Person("Hardik")
print(hardik.name)
hardik.talk()

land = Person("Harsh Landwania")
land.talk()