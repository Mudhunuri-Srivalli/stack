# -------------------------------------------------------
# 1. Duck Typing (Python Polymorphism)
# -------------------------------------------------------

class Dog:
    def sound(self):
        print("Dog barks: Woof Woof")

class Cat:
    def sound(self):
        print("Cat meows: Meow Meow")

class Cow:
    def sound(self):
        print("Cow moos: Moo Moo")

def animal_sound(animal):
    animal.sound()   # Only checks for method name (duck typing)

print("\n--- Duck Typing Example ---")
animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())


# -------------------------------------------------------
# 2. Operator Overloading
# -------------------------------------------------------

class Box:
    def __init__(self, length):
        self.length = length

    # Overload '+' operator
    def __add__(self, other):
        return Box(self.length + other.length)

    # Overload '>' operator
    def __gt__(self, other):
        return self.length > other.length

    def __str__(self):
        return f"Box(length={self.length})"

print("\n--- Operator Overloading Example ---")
b1 = Box(10)
b2 = Box(20)
b3 = b1 + b2
print("b1 + b2 =", b3)
print("Is b2 > b1?", b2 > b1)


# -------------------------------------------------------
# 3. Method Overloading (Achieved using default arguments)
# -------------------------------------------------------

class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

print("\n--- Method Overloading Example ---")
calc = Calculator()
print("add(10) =", calc.add(10))
print("add(10, 20) =", calc.add(10, 20))
print("add(10, 20, 30) =", calc.add(10, 20, 30))


# -------------------------------------------------------
# 4. Method Overriding (Run-Time Polymorphism)
# -------------------------------------------------------

class Vehicle:
    def mileage(self):
        print("Vehicle mileage varies")

class Car(Vehicle):
    def mileage(self):
        print("Car mileage: 15 km/l")

class Bike(Vehicle):
    def mileage(self):
        print("Bike mileage: 40 km/l")

print("\n--- Method Overriding Example ---")
v = Vehicle()
c = Car()
b = Bike()

v.mileage()
c.mileage()
b.mileage()
