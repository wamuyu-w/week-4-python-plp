"""
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). 
However, make each class define move() differently 
(for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""
class car:
    def move():
        print("Car is driving")

class Plane:  
    def move():
        print("Plane is flying:")

class animal:
    def move():
        print("Animal is walking") 

class human:
    def move():
     print("The person is walking")

# calling the various methods in the classes
Plane.move()
car.move()
human.move()
animal.move()