class Student:
    # class/static variable
    school_name="AIMS"
    def __init__(self,name,roll_no):
        # instance variables
        self.name=name
        self.no=roll_no
        # instance method
    def show(self):
        print(self.no,self.name)
        # class method
        @classmethod
        def change_school(cls,new_Name):
           cls.school_name=new_Name
           print(cls.school_name) 
        @staticmethod
        def is_age():
            age1=18
            return age1
        
 # create objects
s1=Student("valli",14)
s2=Student("vamsi",21)
s3=Student("Gowri",22)

print(s1.name)  # can access instance variable via obj
print(s2.no)    # instance variable via obj
print(Student.school_name) # can access class variable via cls
print(s1.school_name) # class variable via obj

# print(Student.name) #thrws error as it has no attributes and cannot access obj via cls
# print(Student.no) #cannot access obj via cls
# Student.show() #needs obj like:self
# Student.show(s1) #manual way pass is possible

# static method
print(Student.is_age(18))

