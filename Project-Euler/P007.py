# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


primes = [2]    # need to add 2 in now otherwise it won't get logged since 2 % 2 = 0
num = 2

while(len(primes) != 10001):
    # print(num)
    for factor in range(2, num):
        if(num % factor == 0):
            break
        elif(factor == (num-1) and num % factor > 0):
            primes.append(num)
    num += 1
    
# gets the last element in the list (nth to last element) aka primes[-2] would get the 2nd to last element in the primes list
print(primes[-1])