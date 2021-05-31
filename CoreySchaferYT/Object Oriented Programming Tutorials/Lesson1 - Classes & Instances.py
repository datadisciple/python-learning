#
# Python OOP Tutorial 1 - Classes & Instances
# https://youtu.be/ZDa-Z5JzLYM
#

# Attributes and Methods can be thought of as data and functions for a class
# Method → a function that is associated w/ a Class

# Class → a blueprint for creating instances
# Instance → in this example, each employee is a unique instance of the Employee class
    # Instace variable → contain data that is unique to each instance

# create an Employee class
class Employee:
    def __init__(self, first, last, pay):
        # self is the instance
        # it is also standard practice/convention to use the 'self' terminology for the first argument
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    # create a method fullname in the Employee class
    def fullname(self): # just like w/ Classes, self is always used as the first agument of a Method
        return '{} {}'.format(self.first, self.last)    # self ensures this method will work w/ all instances


emp_1 = Employee('Lacey', 'Meehan', 75000)
emp_2 = Employee('Freckles', 'Meehan', 65000)

# each instance gets it's own storage location
print(emp_1)
print(emp_2)
print('\n')

print(emp_1.email)
print(emp_2.email)

# Names, email, & pay are all ATTRIBUTES of the Employee Class
# Methods - provide the ability to do some sort of action within the class (ie. print out an employee's full name)

print(emp_1.fullname()) # Note the parentheses are needed because fullname is a method
print(emp_2.fullname())

# Can also call the method from the class
print(Employee.fullname(emp_1)) # NOTE: the instance of the employee now must be specified in the method's argument

