#
# Overview on using integers & floats in Python
# https://youtu.be/khKv-8q7YmY
#

#interger is a whole number, float is a decimal
num = 3
numfloat = 3.14
print(type(num))
print(type(numfloat))
print('\n')

### Arithmetic Operators: 
# Addtion:            3 + 2
# Subtraction:        3 - 3
# Multiplication:     3 * 2
# Division:           3 / 2
# Floor Division:     3 // 2
# Exponent:           3 ** 2
# Modulus:            3 % 2

# Modulo operator % gives remainder after a division
print(3 % 2)

# A common use case for modulo is to determine if a number is Even or Odd
# % 2 → if returns 0, then number is Even. if returns 1, then number is odd.

### Incrementing a variable
num = 1
num = num + 1
num += 1

othernum = 2
othernum *= 5   # sets othernum = to 5x itself
print(othernum)
print('\n')

### Bulit-in functions for working w/ numbers
# absolute value
print(abs(-3))

# round
print(round(3.75))  #by default, rounds to nearest integer value
print(round(3.75, 1))    # specifies to round to 1st digit after decimal
print('\n')

### Comparison Operators - return boolean values
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# Strings can looks like numbers
num_1 = '100'
num_2 = '200.4'
print(num_1 + num_2)

# Cast strings to integers
num_1 = int(num_1)
num_2 = float(num_2)
print(num_1 + num_2)


