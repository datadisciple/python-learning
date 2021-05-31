#
# Python OOP Tutorial 3 - classmethods & static methods
# https://youtu.be/rq8cL2XMM5M
#

### classmethods ###

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod    # this is a classmethod 'decorator' → turns a regular method into a classmethod - allows class to be passed in as the first argument instead of the instance
    def set_raise_amt(cls, amount): # cls is the common convention to use for the classmethod, just like self in a normal method
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # splits string up on the hypen
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # returns the employee object
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # weekday is a python method where Monday is 0, Tuesday is 1, etc.
            return False
        return True


emp_1 = Employee('Lacey', 'Meehan', 75000)
emp_2 = Employee('Freckles', 'Meehan', 65000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('\n')

Employee.set_raise_amt(1.05)    # this is the same as Employee.raise_amount = 1.05 just now the amount is being assigned using a classmethod

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('\n')

# can run the classmethod from the instance, and now it will update class variable for all instances
# in lesson2, since the raise_amount was only being updated for that instance, and not thru a classmethod it didn't affect everything
emp_1.set_raise_amt(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('\n')

# classmethods are often used as alternative constructors
# provides multiple ways to create objects

# ie. pass in a string, and then create an employee based off that string
# from_string classmethod is created in the Employee Class and then used as an alternative constructor

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
print('\n')

#datetime module has a bunch of good examples of using @classmethods as alternative constructors

#-----------------------------------------------------------------------------------------------------------------#

### staticmethods ###

# staticmethods don't pass anything automatically (no 'self, no 'cls', etc.)

# ex. want a simple function that takes in a date and determines if it is a workday
# create a @staticmethod 'is_workday'

import datetime
my_date = datetime.date(2021, 5, 30)    # Sunday
my_date2 = datetime.date(2021, 6, 1)    # Tuesday

print(Employee.is_workday(my_date))
print(Employee.is_workday(my_date2))