# ----------------------------------------
# Python OOP Assignment: All topics up to Inheritance
# ----------------------------------------

# Base Class
class Person:
    species = "Human"         # Class Variable

    def __init__(self, name, age):
        self.name = name      # Instance Variable
        self.__age = age      # Private Variable (Encapsulation)

    # Getter for private variable
    def get_age(self):
        return self.__age

    # Setter for private variable
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    # Instance method
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.__age} years old.")

    # Class method
    @classmethod
    def show_species(cls):
        print("All persons belong to:", cls.species)

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18


# ----------------------------------------
# Single Inheritance
# ----------------------------------------

class Employee(Person):       # Employee inherits Person
    company = "TCS"           # Class variable for Employee

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)     # Calling parent constructor
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("\nEmployee Details:")
        print("Name:", self.name)       # Inherited property
        print("Age:", self.get_age())   # Using getter for private variable
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Company:", Employee.company)


# ----------------------------------------
# Multilevel Inheritance
# ----------------------------------------

class Manager(Employee):    # Manager inherits Employee → Person
    def __init__(self, name, age, emp_id, salary, team_size):
        super().__init__(name, age, emp_id, salary)
        self.team_size = team_size

    def show_manager_info(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.get_age())
        print("Team Size:", self.team_size)
        print("Company:", self.company)


# ----------------------------------------
# Object Creation & Testing
# ----------------------------------------

print("--- Testing Base Class (Person) ---")
p1 = Person("Rahul", 22)
p1.introduce()
Person.show_species()
print("Is adult:", Person.is_adult(22))

print("\n--- Testing Single Inheritance (Employee) ---")
e1 = Employee("Meena", 30, "E102", 55000)
e1.show_details()

print("\n--- Testing Multilevel Inheritance (Manager) ---")
m1 = Manager("Sonia", 35, "M501", 90000, 10)
m1.show_manager_info()

