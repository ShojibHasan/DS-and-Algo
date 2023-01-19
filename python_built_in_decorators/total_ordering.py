# @total_ordering: A Class Decorator That Fills In Missing Ordering Methods
'''
The @total_ordering decorator from the functools module is used to generate the missing comparison methods for a Python class based on the ones that are defined.

It can make your code cleaner and save your time. Since you dont need to write all the comparison methods.

Some old classes may not define enough comparison methods. Its safer to add the @total_ordering decorator to it for further usage.

'''

from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade


student1 = Student("Alice", 85)
student2 = Student("Bob", 75)
student3 = Student("Charlie", 85)

print(student1 < student2)  # False
print(student1 > student2)  # True
print(student1 == student3)  # True
print(student1 <= student3) # True
print(student3 >= student2) # True