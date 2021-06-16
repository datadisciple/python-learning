# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import time, math
start_time = time.time()

number = 600851475143
bottom_div = []
top_div = []
divisors = []

# find the bottom half of the divisors
for num in reversed(range(1, int(math.sqrt(number+1)))):    #reversed() function allows backwards iteration over the range
    
    if (number%num == 0):
        bottom_div.append(num)

# find the top half of the divisors
for halfpair in bottom_div:
    top_div.append(int(number/halfpair))

# add the bottom half and top half together into a full divisors list
divisors = bottom_div + top_div

# sort divisors list in descending order
divisors.sort(reverse=True)

# cycle through each divisor and see if it is divisible by anything
for div in divisors:
    largestprime = 0

    for i in range(2, div):
        # if divisble, break out of loop and move onto next divisors
        if(div%i == 0):
            break
        # if there were no numbers divisor was divisble by then this is the largest prime since divisors list has been sorted from greatest to least
        elif (i == div-1):
            largestprime = div
            break

    # no need to looks at the rest of the divisors if the largest has already been found
    if (largestprime > 0):
        break

print(divisors)
print(largestprime)
print("--- %s seconds ---" % (time.time() - start_time))