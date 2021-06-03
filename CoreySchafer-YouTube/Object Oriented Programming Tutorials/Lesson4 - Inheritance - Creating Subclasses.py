#
# Python OOP Tutorial 4 - Inheritance - Creating Subclasses
# https://youtu.be/RSl87lqOXDE
#

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


# Create Developer subclass

class Developer(Employee):  # putting Employee in the parentheses means inherit all functionality of the Employee class (all attributes & methods)
    # change the raise amount for a developer
    # NOTE: the raise amount in the employee (parent) class is unaffected and stays at 1.04
    raise_amount = 1.10

    # add programming language as an input for developers
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # this passes first, last and pay to the Employee's init method & let that class handle those arguments
        self.prog_lang = prog_lang  # handle the new input as normal


# Create Manager subclass

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):   # set employees default to None (null) if nothing is passed in
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())   # remember fullname() is a method of the parent/Employee class


dev_1 = Developer('Katie', 'Meehan', 80000, 'Python')
dev_2 = Developer('Bear', 'Meehan', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)
print('\n')

# Using help provides a good visual of the chain on inheritance
# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print('\n')

mgr_1 = Manager('Chippy', 'Chipmunk', 90000, [dev_1])

print(mgr_1.email)

# add employee to manager 1
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print('\n')

# remove employee from manager 1
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
print('\n')

#
#

# isinstance() tells if object is an instance of a class
print(isinstance(mgr_1, Manager))    # checks whether mgr_1 is an instance of the Manager class → True
print(isinstance(mgr_1, Employee))  # checks whether mgr_1 is an instance of the Employee class → True (since it is a subclass of Employee)
print(isinstance(mgr_1, Developer)) # checks whether mgr_1 is an instrance of the Developer class → False
print('\n')

# issubclass() tells if class is a subclass of another class
print(issubclass(Developer, Employee))   # checks if Developer is a subclass of Employee → True)
print(issubclass(Manager, Developer))   # checks if Manager is a subclass of Developer → False


# exceptions.py from the WSGY library is good code to reference for examples of class inheritance