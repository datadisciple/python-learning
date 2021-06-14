# Perfect Number → number whose divisors sum to equal it
# 28: 1, 2, 4, 7, 14 = 28

# A number is called deficient or abundant if the sum of divisors is less than or greater than the number

# It is known that all integers greater than 28123 can be written as the sum of two abundant numbers
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers

import time

start_time = time.time()

abundant_nums = []
pos_nums = []
limit = 28123

for num in range(1, limit+1):
    sum_div = 0
    divisors = []

    for j in range(1, num):
        if num % j == 0:
            sum_div += j
            divisors.append(j)

    # if sum of divisors is greater than the number, add to abundant numbers list
    if sum_div > num:
        abundant_nums.append(num)        

    # create list of all positive numbers
    pos_nums.append(num)

r_ind =0

# loops through abundant numbers and removes any values in pos_nums list that are made by adding together
for a in abundant_nums:
    for b in abundant_nums:
        if(a+b) in pos_nums:
            pos_nums.remove(a+b)
            r_ind += 1
            print(f'removed {str(r_ind)}')  # this is just a sanity print to ensure code is still doing something since it takes forever to run
        elif(a+b)>limit: break

answer = sum(pos_nums)
print(answer)
print("--- %s seconds ---" % (time.time() - start_time))    # current runtime is extremely slow → 841.7 seconds


