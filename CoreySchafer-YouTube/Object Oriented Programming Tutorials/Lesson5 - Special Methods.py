#
# Python OOP Tutorial 5 - Special (Magic/Dunder) Methods
# https://youtu.be/3ohzBxoFHAY
#

# Special Methods are always surrounded by doubles underscores __init__
# They are often referred to as Dunder (ie. dunder init)

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

    # Special Methods
    # __repr__ is meant to be an unambigious representation of the object
    # should be used for debugging, logging, etc. (for other developers)
    # always best to have this as a minimum, as a call to __str__ will use __repr__ as a fall back
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    # __str__ is meant to be a readable representation of the object
    # to provide a readable display to the end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # add 2 employees together such that the result is there combined salaries
    # use a dunder add method
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
emp_1 = Employee('Lacey', 'Meehan', 75000)
emp_2 = Employee('Freckles', 'Meehan', 65000)

# prints out returned string specified in the __repr__ method if that is the only one specified
# prints out returned string specified in the __str__ method if both are specified
print(emp_1)
print('\n')

# prints out the same thing - two different ways to call these special methods
print(repr(emp_1))
print(emp_1.__repr__())

print(str(emp_1))
print(emp_1.__str__())
print('\n')

print(1+2)
print(int.__add__(1,2)) # dunder add method - allows you to customize how addition works for your objects

# tests dunder add method specified in Employee class
print(emp_1+emp_2)
print('\n')

# there are all kinds of special methods for arithmetic
# Reference → Python 3.3.7 "Emulating numeric types" documention

print(len('test'))
print('test'.__len__())

print(len(emp_1))

# datetime module (datetime.py) has good real-world examples of special modules
