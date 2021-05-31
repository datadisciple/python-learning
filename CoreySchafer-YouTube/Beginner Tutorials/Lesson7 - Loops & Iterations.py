#
# Overview on for loops & while loops
# https://youtu.be/6iF8Xb7Z3wQ
#

# For Loops
print('[For Loops]')

nums = [1, 2, 3, 4, 5]

for num in nums:    # each time through the loop, the num variable is equal to that next item in the list
    print(num)
print('\n')

# 'break' exits out of a loop
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)  # Note: 3 is note printed out bc we broke out of the loop before this print statement
print('\n')

# 'continue' jumps to next iteration in loop
for num in nums:
    if num == 3:
        print('Found!')
        continue    # continues onto next iteration in loop and doesn't do any of the other tasks at current iteration
    print(num)
print('\n')

# Nested Loops
for num in nums:
    for letter in 'abc':
        print(num, letter)
print('\n')

# use range() to loop over a certain range
# first value is inclusive, second value is exclusive
for i in range(10): # prints up to but not including 10
    print(i)
print('\n')

for i in range(1,11):
    print(i)
print('\n')

# While Loops - will go on until condition evaluates to false
#
# if not careful these could go on forever!
# incrementing is important for these

print('[While Loops]')

x = 0

while x < 10:
    print(x)
    x += 1  # increment statement

# Sometimes there is a benefit to creating an infinite loop that will not break out until a certain value is seen

# press CTRL + C to exit out of a terminal that is stuck running an infinite loop

