# Functional Requirements - Person 
# • Every person should have: name, age 
# • Role must be defined using abstraction: Student / Teacher

# Educational Institution Management System
from abc import ABC, abstractmethod


# Abstract Person Class

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass


# Student Class

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.enrolled_courses = []   # List of Course objects

    def role(self):
        return "Student"

    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.students.append(self)

    def list_courses(self):
        print(f"\nCourses enrolled by {self.name}:")
        if self.enrolled_courses:
            for c in self.enrolled_courses:
                print(f"- {c.course_name} ({c.course_code})")
        else:
            print("No courses enrolled.")


# Teacher Class

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.assigned_courses = []   # List of Course objects

    def role(self):
        return "Teacher"

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.teacher = self

    def list_assigned_courses(self):
        print(f"\nCourses taught by {self.name}:")
        if self.assigned_courses:
            for c in self.assigned_courses:
                print(f"- {c.course_name} ({c.course_code})")
        else:
            print("No assigned courses.")



# Course Class

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = None
        self.students = []      # List of Student objects

    def set_teacher(self, teacher):
        self.teacher = teacher
        teacher.assign_course(self)

    def enroll_student(self, student):
        student.enroll(self)

    def course_info(self):
        print(f"\nCourse Information:")
        print(f"Name: {self.course_name}")
        print(f"Code: {self.course_code}")

        if self.teacher:
            print(f"Teacher: {self.teacher.name}")
        else:
            print("Teacher: Not assigned")

        print("Enrolled Students:")
        if self.students:
            for st in self.students:
                print(f"- {st.name} (ID: {st.student_id})")
        else:
            print("No students enrolled.")


# Department Class

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.courses = []
        self.teachers = []

    def add_course(self, course):
        self.courses.append(course)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def department_info(self):
        print(f"\nDepartment: {self.dept_name}")
        print("Courses:")
        for c in self.courses:
            print(f"- {c.course_name} ({c.course_code})")

        print("\nTeachers:")
        for t in self.teachers:
            print(f"- {t.name} (ID: {t.teacher_id})")


# Administration Class

class Administration:
    def assign_teacher_to_course(self, teacher, course):
        course.set_teacher(teacher)

    def enroll_student_to_course(self, student, course):
        course.enroll_student(student)


# Running the System (Test Case)

if __name__ == "__main__":
    # Create Students
    s1 = Student("Rahul", 20, "S101")
    s2 = Student("Anjali", 21, "S102")

    # Create Teachers
    t1 = Teacher("Mr. Sharma", 40, "T501")

    # Create Courses
    c1 = Course("Mathematics", "MTH101")
    c2 = Course("Physics", "PHY201")

    # Department
    dept = Department("Science")
    dept.add_course(c1)
    dept.add_course(c2)
    dept.add_teacher(t1)

    # Administration actions
    admin = Administration()
    admin.assign_teacher_to_course(t1, c1)
    admin.enroll_student_to_course(s1, c1)
    admin.enroll_student_to_course(s2, c1)
    admin.enroll_student_to_course(s1, c2)

    # Display Results
    dept.department_info()
    t1.list_assigned_courses()
    s1.list_courses()
    c1.course_info()



# Educational Institution Management System (Full OOP Implementation)

from abc import ABC, abstractmethod


# ABSTRACT CLASS: PERSON (Abstraction)

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass


# STUDENT CLASS (Inheritance from Person)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.__courses = []    # Encapsulated list

    def get_role(self):
        return "Student"

    def enroll_course(self, course):
        if course in self.__courses:
            print(f"[ERROR] Student {self.name} already enrolled in {course.course_name}")
        else:
            self.__courses.append(course)
            course.enroll_student(self)

    def list_courses(self):
        if not self.__courses:
            print(f"{self.name} is not enrolled in any courses.")
            return
        print(f"Courses enrolled by {self.name}:")
        for c in self.__courses:
            print(f"- {c.course_name} ({c.course_code})")



# TEACHER CLASS (Inheritance from Person)

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.__assigned_courses = []  # Encapsulated

    def get_role(self):
        return "Teacher"

    def assign_course(self, course):
        if course in self.__assigned_courses:
            print(f"[ERROR] Teacher {self.name} already assigned to {course.course_name}")
        else:
            self.__assigned_courses.append(course)
            course.set_teacher(self)

    def list_assigned_courses(self):
        if not self.__assigned_courses:
            print(f"{self.name} is not assigned to any courses.")
            return
        print(f"Courses assigned to {self.name}:")
        for c in self.__assigned_courses:
            print(f"- {c.course_name} ({c.course_code})")


# COURSE CLASS

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = None
        self.__students = []  # Encapsulation

    def set_teacher(self, teacher):
        self.teacher = teacher

    def enroll_student(self, student):
        if student in self.__students:
            print(f"[ERROR] Student {student.name} already in course {self.course_name}")
        else:
            self.__students.append(student)

    def course_info(self):
        print(f"\nCourse: {self.course_name} ({self.course_code})")
        print(f"Teacher: {self.teacher.name if self.teacher else 'Not Assigned'}")
        print("Students Enrolled:")
        for s in self.__students:
            print(f"- {s.name} ({s.student_id})")

# DEPARTMENT CLASS

class Department:
    def __init__(self, name):
        self.department_name = name
        self.courses = []
        self.teachers = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def summary(self):
        print(f"\n===== Department: {self.department_name} =====")
        print("\nCourses:")
        for c in self.courses:
            print(f"- {c.course_name} ({c.course_code})")

        print("\nTeachers:")
        for t in self.teachers:
            print(f"- {t.name} ({t.teacher_id})")

        print("\nStudents:")
        for s in self.students:
            print(f"- {s.name} ({s.student_id})")
        print("=============================================")


# ADMINISTRATION CLASS

class Administration:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def department_info(self):
        print("\n=== Institution Departments ===")
        for dep in self.departments:
            print(f"- {dep.department_name}")



# SAMPLE USE CASES

if __name__ == "__main__":

    # Create Administration
    admin = Administration()

    # Create Department
    cs_dept = Department("Computer Science")
    admin.add_department(cs_dept)

    # Create Courses
    ds = Course("Data Structures", "CS101")
    algo = Course("Algorithms", "CS102")

    cs_dept.add_course(ds)
    cs_dept.add_course(algo)

    # Create Teachers
    t1 = Teacher("Alice", 40, "T001")
    t2 = Teacher("Bob", 38, "T002")

    cs_dept.add_teacher(t1)
    cs_dept.add_teacher(t2)

    # Create Students
    s1 = Student("John", 20, "S001")
    s2 = Student("Jane", 21, "S002")

    cs_dept.add_student(s1)
    cs_dept.add_student(s2)

    # Assign teachers to courses
    t1.assign_course(ds)
    t2.assign_course(algo)

    # Enroll students in courses
    s1.enroll_course(ds)
    s1.enroll_course(algo)

    s2.enroll_course(ds)

    # Retrieve Information
    cs_dept.summary()
    ds.course_info()
    algo.course_info()

    s1.list_courses()
    t1.list_assigned_courses()

    admin.department_info()
