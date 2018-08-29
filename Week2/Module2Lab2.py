"""
Author: Jim Jenkins (dvlupr)
Date: 06/27/2018

Get a random number:
DO EITHER
 -  create a variable called test_number with a number between 50 and 100 in it
 - Assign a random number between 50 and 100 to a variable called test_num (read page 50-52 in your text)
If test_num is divisible by three, print "fizz"
If test_num is divisible by five, print "buzz"
if test_num is divisible by both three and five, print "fizzbuzz!"
if test_num does not meet any of the above criteria, print test_num
"""

import random

# random number

rn = random.randint(1,51)

# assign test_num to random number
test_num = rn

# run variable
test_num3 = test_num % 3
test_num5 = test_num % 5

# print to see output
print('random number: ', rn)
print('test_num3: ', test_num3)
print('test_num5: ', test_num5)

#FizzBuzz logic
if test_num3 == 0 and test_num5 == 0:
    print('fizzbuzz')
elif test_num3 == 0:
    print('fizz')
elif test_num5 == 0:
    print('buzz')
else:
    print(test_num)
