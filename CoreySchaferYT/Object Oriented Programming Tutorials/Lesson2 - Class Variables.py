#
# Python OOP Tutorial 2 - Class Variables
# https://youtu.be/BJ-VvGyQxho
#


class Employee:

    # Class Variable - shared among ALL instances of a class
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        # Instance Variables - unique to each instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # each time a new employee is added, increment class variable num_of_emps by 1
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # raise_amount could also be accessed using the class Employee.raise_amount, but then that would not allow a unique raise amount to be set for a certain instance

emp_1 = Employee('Lacey', 'Meehan', 75000)
emp_2 = Employee('Freckles', 'Meehan', 65000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print('\n')

# prints out the name space of emp_1
print(emp_1.__dict__)

#prints out the name space of Employee class - raise_amount is now seen
print(Employee.__dict__)
print('\n')

# Can call on raise amount either through the Eemployee class or a specific instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('\n')

# If you change the raise amount value via the Employee class, it will update for all instances
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('\n')

# If you change the raise amount value via an instance....
# it will update only for that instance and now raise_amount will be added to emp_1's namespace
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print('\n')

print(Employee.num_of_emps)
