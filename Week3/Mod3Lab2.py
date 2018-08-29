"""
Author: Jim Jenkins (devupr@uw.edu)
Date: 07/11/2018't match see if it's higher or lower than the number and print a hint
"""

import random
for x in range(10):
  random_number = random.randint(1,11)

user_guess = 0
maximum_guess = 3
guess_count = 0

while guess_count < maximum_guess:
    guess_count = guess_count + 1

    user_guess = (int(input('What is your first guess? ')))
    if user_guess < random_number:
        print('Your guess is low, try again.')
    elif user_guess > random_number:
        print('Your guess is high, try again.')
    else:
        print('That is my number!')
        break