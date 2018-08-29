#!/usr/bin/env python

"""
Ask the user three original questions and store their input as variables
Combine the three answers into a sentence of your choosing
Print out the final combined sentence using one of the string operations
Add docstrings and comments to your code
Upload your script to canvas (optional: include a link to GitHub version).

Stretch: Create a function that contains the print statement (pass the
variables in as arguments to use in the print function).
"""

# story set-up
print('The Gorge of Eternal Peril')
print('STOP! He who wishes to cross the Bridge of Death must answer me these questions three...')
print('-----')


# store user name, quest, and favorite color
user_name = input('What is your name?: ')
quest = input('what is your quest?: ')
favorite_color = input ('What is your favorite color?: ')


# reply with the end of the story
print('-----')
print('Hard coded version:')
print('Well,', user_name, 'as you seek your quest of', quest, 'you\'re favorite color of', favorite_color, 'is correct!')
print('So off you go.')


"""stretch"""


# function create the parameterized version of the story
def fn_gorgeofperil(param1, param2, param3):
      print('Well,', param1, 'as you seek your quest of', param2, 'you\'re favorite color of', param3,
            'is correct!')


# run function and end the story
print('-----')
print('Function version:')
fn_gorgeofperil(user_name, quest, favorite_color)
print('So off you go.')
