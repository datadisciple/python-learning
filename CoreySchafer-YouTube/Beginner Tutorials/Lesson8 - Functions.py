#
# Overview on creating, defining, and using functions
# https://youtu.be/9Os0o3wzS_I
#

# pass → if you have an empty function, c an fill it in w/ 'pass' and it will allow the program to run without throwing an error

def hello_func():
    print('Hello Function!')

# runs function 4x → prints 4x
for run_func in range (0,4):
    hello_func()

def hello_func2():
    return('Hello Function2!')

hello_func2() # this will not print anything because the function is setup with a return
print(hello_func2())    # if you actually want to print the return use a print statement before calling the function

# since the function returns a string, other string functions can be chained onto it
print(hello_func2().upper())

def hello_func3(greeting, name = 'You'):    # if no value is passed in for 'name', it uses the default 'You'
    return '{}, {}!'.format(greeting, name)
    # can also return using an f-string instead of .format approach

# NOTE: required positional arguments must come before keyword (optional) arguments

print(hello_func3('Hi'))
print(hello_func3('Sup', 'dude'))
print('\n')

# * and ** are used when the # of positional or keyword arguments is unknown
# don't have to call the function inputs args & kwargs, but it is convention/best practice
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)    # NOTE: the args is returned as a tuple, and kwargs a dictionary
print('\n')

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# can pass lists/tuples and dictionaries into the function for args and kwargs respectively using * & **
# it will unpack the values and pass them in individually
student_info(*courses, **info)
print('\n')

#------------------------------------------------------------------------------------------------------------#
#
# 👇 Function example that also hits on previously covered fundamentals 👇
#

# Number of days per month as a list. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years.""" # """docstring""" →  documents what a function or class is suppoed to do; good practice

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017,2))
print(days_in_month(2020, 2))
