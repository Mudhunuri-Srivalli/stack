#oops=>
#data security
#real world applications
#maintainability 


#class and object
#variables and methods
# class Calculator:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b):
#         print(a-b)
# cla1=Calculator()
# cla2=Calculator()
# cla3=Calculator()
# cla4=Calculator()
# cla3.add(2,3)
    


# Create your own class which can implement all arthematic operations. Create 2 objects for it and call above implemented methods. Add model_num, made_in variables to obj1. Add color and discount to obj2. print model_num, made_in, color, discount to both the object

# Creating a Class with Arithmetic Operations
class Calculator:

    # Addition
    def add(self, a, b):
        return a + b

    # Subtraction
    def sub(self, a, b):
        return a - b

    # Multiplication
    def mul(self, a, b):
        return a * b

    # Division
    def div(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


# -----------------------------
# Creating two objects
# -----------------------------
obj1 = Calculator()
obj2 = Calculator()

# Adding extra attributes to obj1
obj1.model_num = "Model X120"
obj1.made_in = "India"

# Adding extra attributes to obj2
obj2.color = "Black"
obj2.discount = "15%"

# -----------------------------
# Calling arithmetic methods
# -----------------------------
print("Addition:", obj1.add(10, 5))
print("Subtraction:", obj1.sub(10, 5))
print("Multiplication:", obj2.mul(6, 4))
print("Division:", obj2.div(20, 4))

# -----------------------------
# Printing attributes
# -----------------------------
print("\n--- Object 1 Details ---")
print("Model Number:", obj1.model_num)
print("Made In:", obj1.made_in)

print("\n--- Object 2 Details ---")
print("Color:", obj2.color)
print("Discount:", obj2.discount)

# output:
# Addition: 15
# Subtraction: 5
# Multiplication: 24
# Division: 5.0

# --- Object 1 Details ---
# Model Number: Model X120
# Made In: India

# --- Object 2 Details ---
# Color: Black
# Discount: 15%

    
