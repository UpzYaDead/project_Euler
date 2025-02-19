from time import *
import math
start = time()


#
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

#plan: just create all triangular numbers, and immediately check how many divisors it has, if the number itself it less than 500, we don't have to check it
#for the number of divisors.

#you really have to avoid a double for loop...

def triangular_numbers(divisor):
    triangle_num,count=0,0
    dictionary={}
    for i in range(1,1000000): #just pick some ridiculous large number, we will break anyway once we found the number with 500+ divisors
        dictionary[triangle_num] = count
        triangle_num+=i
        count=0
        j=1
        while j <= math.sqrt(triangle_num):
            if triangle_num % j ==0:
                if triangle_num % i == i: #there is only one divisor
                    count+=1
                else:
                    count+=2
            j+=1
            if count == divisor:
                return triangle_num

    return dictionary

print(triangular_numbers(500))

end = time()
print("Time elapsed:", end-start)
