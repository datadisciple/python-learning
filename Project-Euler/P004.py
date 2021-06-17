# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def main(x, y):
    palindrome = 0

    for num1 in range(x, y):
        for num2 in range(x, y):
            product = num1*num2
            digits = int(math.log10(product) + 1)   # could calc digits using len(str(product)), but this is slower

            # if product is an even # of digits
            if digits % 2 == 0:
                beg = str(product)[:int(digits/2)]    # note: need to convert to int bc division of int by int results in a float in Python3
                end = str(product)[int(digits/2):]
                rev_end = ''.join(reversed(end))    # reverses string by joining reverse against nothing, could also do end[::-1]


                if (beg == rev_end and product > palindrome):
                    palindrome = product
                    mult1 = num1
                    mult2 = num2
            
            # else product is an odd number of digits
            else:
                middle = int(digits/2 + 1)
                beg = str(product)[:middle]
                end = str(product)[middle:]
                rev_end = ''.join(reversed(end))

                if (beg == rev_end and product > palindrome):
                    palindrome = product
                    mult1 = num1
                    mult2 = num2

    # return list w/ largest palindrome and the two numbers that were multiplied together to form it            
    return [palindrome, mult1, mult2]          



if __name__ == "__main__":
    # just testing user input functionaliry
    var1 = int(input('First number in range: '))
    var2 = int(input('Last number in range:'))+1
    print(main(var1, var2))
