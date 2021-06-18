# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# NOTE: This is a solution but a very slow one

import time, math
start_time = time.time()

smallest = False
num = 2520

while smallest == False:
    num += 2520 # answer is going to have to be some multiple of 2520 since that is the smallest number divisble by the first 10
    print(num)

    # prime checks - used to cut down on looping
    if (num % 11 > 0): continue
    if (num % 13 > 0): continue
    if (num % 17 > 0): continue
    if (num % 19 > 0): continue

    # only care about this range bc if divisble in this range it will also be divisble by the other numbers in range
    for div in range(13, 19):
        rem = num % div

        if rem > 0:
            break

        elif div == 18 and rem == 0:            
            smallest = True # signal answer found and break out of loop so while loop reads that smallest is now true
            break

print('Answer: ' + str(num))

# Execution time
print("--- %s seconds ---" % (time.time() - start_time))