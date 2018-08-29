

"""
Create a script called hw3.py
Ask the user to enter a starting and ending number

The user must not enter a starting number less than 1
The user must enter an ending number at least 5 times greater than the starting number

Create checks and error messages for the above

Create a list of integers in the range of the user's starting and ending numbers

Print out the number and index of each item in the list that is even
Sum all the odd numbers in the list using a for loop ( hint: append odd numbers to a list and then sum() that list )
Print out the cumulative sum calculated above
Wrap your steps in a function and call the function
Upload your python file to Canvas.

Please enter a starting number: 2

Please enter an ending number: 200

Even numbers in your list:

2 is at the 3rd index

4 is at the 5th index...

The sum of your number list is: 500 (I made that number up)
"""

# Ask the user to enter a starting and ending number
start_num = int(input('Please enter a starting number: '))
end_num = int(input('Please enter an ending number: '))

test_num = start_num * 5


# The user must not enter a starting number less than 1
# The user must enter an ending number at least 5 times greater than the starting number
if start_num < 1:
    print('Really? You entered a starting number less than 1, go ahead try again.')
elif end_num <= test_num:
    print('The end number you entered is not large enough, go ahead and try again.')
else:
    print('Nice job!')


print('----')
print('start', start_num)
print('end:', end_num)
print('test:', test_num)
print('----')

# Create a list of integers in the range of the user's starting and ending numbers

for nums in range(start:start_num, end:end_num):
