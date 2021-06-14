# Perfect Number → number whose divisors sum to equal it
# 28: 1, 2, 4, 7, 14 = 28

# A number is called deficient or abundant if the sum of divisors is less than or greater than the number

# It is known that all integers greater than 28123 can be written as the sum of two abundant numbers
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers

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

    # if abundant record in dict as True, and enter num into abundant_num list
    if sum_div > num:
        abundant_nums.append(num)
        # print(num)
        # print(divisors)
        # print(sum_div)
        # print('\n')
        

    if(num % 2 == 0):
        pos_nums.append(num)

# print(abundant_nums)
# print(pos_nums)
# print('\n')

"""for a in abundant_nums:
    for b in abundant_nums:
        if (a+b) in pos_nums:
            finder = pos_nums.index(a+b)
            pos_nums[finder] = 0
        if ((a+b) > limit): break"""

for a in abundant_nums:
    if (2*a in pos_nums):
        pos_nums.remove(2*a)

final_pos_nums = pos_nums

for value in pos_nums:
    for a in abundant_nums:
        if(value not in final_pos_nums): break

        for b in abundant_nums:
            if (a+b)==value:
                final_pos_nums.remove(value)
                break


"""for k, value in enumerate(pos_nums):

    for a in abundant_nums:
        if (value not in pos_nums): break

        for b in abundant_nums:
            if ((a+b) == value and value in pos_nums):
                pos_nums[k]=0
                break"""
    
answer = sum(final_pos_nums)
# print(pos_nums)
print(answer)

""" for i in range(1,51):
    if (i % 2 == 0):
        pos_nums.append(i)
        
        for a in abundant_nums:
            if (2*a > i): break

            for b in abundant_nums:
                if ((a+b) == i and i in pos_nums):
                    pos_nums.remove(i) """

