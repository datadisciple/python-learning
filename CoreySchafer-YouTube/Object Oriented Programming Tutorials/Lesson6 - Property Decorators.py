#
# Python OOP Tutorial 6 - Property Decorators - Getters, Setters, and Deleters
# https://youtu.be/jCzT9XFZ5bw
#

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   # adds a property aka getter decorator to the method so it gets treated like an attribute
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # setter decorater → allows fullname to be used as a setter to set first name and last name of employee object
    @fullname.setter
    def fullname(self, name):    # where name is the value trying to be set
        first, last = name.split(' ')   # splits the name passed in into two parts based on space
        self.first = first
        self.last = last

    # deleter decorater
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Lacey', 'Meehan')

# NOTE: w/o a property decorator, the email original email attribute would still reference 'Lacey' as the first name as it was set when the employee was defined
emp_1.first = 'Jim'

# this call works once the fullname() method is turned into a setter decorator
emp_1.fullname = 'Sean Meehan'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print('\n')

# test out deleter decorator for fullname
del emp_1.fullname

