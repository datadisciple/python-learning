#
# Overview on using import modules & exploring the standard library
# https://youtu.be/CqvZ3vGoGs0
#

# when you import a file it automatically runs all the code from the function it imports
# this is how it defines all the function and variables in that file

import Lesson9module as L9mod # can be imported directly since it's in the same directory as this file
from Lesson9module import find_index, test # imports only the find_index function & 'test' variable
# from my module import * → this would import everything from the module but this approach is generally frowned upon bc it can be hard to tell what came from the imported module and what didn't

import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

# need to type module name, then what you want to grab from the module (ie. a function, varaible, etc.) in order to use it
index = L9mod.find_index(courses, 'Math')
print(index)

# unless you import the function specfically (see ln 10)
index = find_index(courses, 'Physics')
print(index)
print(test + '\n')

# this is the list of directories that python is looking for modules in when an import is run
print(sys.path)
print('\n')

# Directories get added in this order
    # 1) Directory containing the script that is being run
    # 2) Directories listed in the python path environment variable
    # 3) Standard library directories
    # 4) Site packages directory for 3rd party packages

# if module does not live in current directory it can be appended to the system path that is search when the import module runs
# NOTE: this is not the best approach bc directory often needs to be appended before other imports
# and it's not the best idea to have to manually hardcode this in multiple locations
sys.path.append('c:\\Users\\Sean Meehan\\Desktop\My-Modules')
print(sys.path)
print('\n')

# Instead, you can make this directory change in the next place sys.path looks → the python path environment variable
# For Windows:
    # System > About > Advanced System Settings > Environment Variable
    # Create a 'new' environment variable for Sean Meehan
    # Give it a name (ie. PYTHONPATH)
    # Give it a value (C:\Users\Sean Meehan\Desktop\My-Modules)

# Different text editors can behave differently w/ how they allow you to add environment varibles
# Search editor name + pythonpath when in doubt and that should bring up the necessary resources/instructions

#------------------------------------------------------------------------------------------------------------#
#
### Standard Libraries

import random
random_course = random.choice(courses)
print(random_course)
print('\n')

import math
rads = math.radians(90)
print(math.sin(rads))
print('\n')

import datetime
import calendar
today = datetime.date.today()   # today's date
print(today)
print(calendar.isleap(2020))    # checks if 2020 is a leap year → it is so isleap() returns true
print('\n')

import os   # gives access to underlying operating system
print(os.getcwd())  # prints out current working directory where script is located

# OS module is pretty powerful - can scan file system, create files, delete files, etc.

print(os.__file__) # prints location where standard library lives

import antigravity  # this is a bit of a joke in the python community. opens up a webpage to the comic on import.

### exploring standard libraries can be a good way to learn
