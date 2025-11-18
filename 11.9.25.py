# from abc import ABC,abstractmethod
# class person(ABC):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @abstractmethod
#     def get_role(self):
#         pass

# class Student(person):

#         def __init__(self,student_id,name,age):
#             super().__init__(name,age)
#             self.student_id=student_id
#             self.enrolled_courses=[]
#         def get_role(self):
#             return "student"
#         def get_enrolled_courses(self):
#             print(self.enrolled_courses)
#         def add_a_courses(self,course_name):
#              self.enrolled_courses.append(course_name)

# stu1=Student(19,"valli",22)
# print(stu1.name)
# stu1.get_enrolled_courses()
# stu1.add_a_courses('DBMS')
# stu1.add_a_courses('OOPS')
# stu1.add_a_courses('OS')
# stu1.get_enrolled_courses()






# class course:
#      def __init__(self,course_name,course_code):
#           self.course_name=course_name
#           self.course_code=course_code
#           self.teacher=none




# PYTHON CONDITIONAL STATEMENTS
# 1. if Statement
age = 18
if age >= 18:
    print("Eligible!")

# 2. if-else
x = 10
if x > 0:
    print("Positive")
else:
    print("Negative")

# 3. if-elif-else
marks = 75
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")

# 4. Nested if
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")

# 5. Short-hand if
print("Even") if x % 2 == 0 else print("Odd")


# FULL OOP CONCEPTS IN PYTHON
# 1️⃣ Class & Object
class Car:
    def start(self):
        print("Car starts")

c = Car()
c.start()

# 2️⃣ Constructor (__init__)
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# 3️⃣ Encapsulation (Private variables)
class Bank:
    def __init__(self):
        self.__balance = 0  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# 4️⃣ Inheritance
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# 5️⃣ Polymorphism
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

# 6️⃣ Abstraction
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def work(self):
        pass

# 7️⃣ Method Overloading (Python style)
class Calc:
    def add(self, a=None, b=None, c=None):
        if c is not None:
            return a + b + c
        return a + b

# 8️⃣ Method Overriding
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

# 9️⃣ Multiple Inheritance
class A: pass
class B: pass
class C(A, B): pass

# 🔟 Composition
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
