#
# Example file for working with functions
#

# define a basic function
# the : starts the scope which lasts as long as the indentation
def func1():
  print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
  print(arg1, " ", arg2)


# function that returns a value
def cube(x):
  return x*x*x

# function with default value for an argument
def power(num, x=1):
  result = 1
  for i in range(x):
    result = result * num
  return result

#function with variable number of arguments (must be last parameter and use *)
def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result


# testing workspace
func1()
print (func1()) #prints 'I am a function' & then prints 'None' since there is no return specified in the functions evaluation
print (func1) #prints address of function

func2(10,20)
print(func2(10,20)) 
print (cube(3))

print (power(2))
print (power(2,3))
print (power(x=3, num=2)) #python lets you call functions with inputs in any order as long as you supply their correct named parameters

print(multi_add(4,5,10,4)) #can change number of inputs since the function parameter was defined with a *
print(multi_add(5,2))