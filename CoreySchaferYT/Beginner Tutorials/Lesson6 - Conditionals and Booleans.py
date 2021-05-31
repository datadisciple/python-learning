#
# Overview on conditionals & booleans
# https://youtu.be/DZwmZ8Usvnk
#

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Python'

# elif is the same as else if in other languages
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

# Note: there are no switch/case statements in python
# Python likes to keep it simple (KISS)

# Boolean Operations:
# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

logged_in = False

if not logged_in:   # not is the same thing as saying if logged_in = false
    print('Please Log In')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # returns True bc values in list are equal
print(a is b)   # returns False bc these are two different locations in memory

print(id(a))    # prints id in memory
print(id(b))

b = a   # setting b = a aka they are now the same objects in memory
print(a is b)   # this now returns True bc these are the same objects in memory

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {} → empty dictionary

# Anything else by default evaluates to True

condition = None    # None evaluates to False (same w/ 0, empty sequence, etc.)

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# Useful to use a boolean check to check if a sequence is empty or not
