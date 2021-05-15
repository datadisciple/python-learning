# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# re-claring the variable works
f="abc"
print(f)


# ERROR: variables of different types cannot be combined
# python is a strongly typed language & values need to be converted to same type before they can be added together
print("this is a string " + str(123))


# Global vs. local variables in functions
# a function gets its own local copy of any variables that are declared inside it
# have to tell function a variable is global in order to effect its value outside of function
def someFunction():
  global f
  f="def"
  print(f)

someFunction()
print(f)

# undefine a variable
del f
print(f) #this prints out an error because the variable is now undefined

