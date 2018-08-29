#!/usr/bin/env python

"""
Ask the user three original questions and store their input as variables
Combine the three answers into a sentence of your choosing
Print out the final combined sentence using one of the string operations
Add docstrings and comments to your code
Upload your script to canvas (optional: include a link to GitHub version).
"""

# story set-up
print('The Gorge of Eternal Peril')
print('STOP! He who wishes to cross the Bridge of Death must answer me these questions three...')

# store the programmers favorite color
programmer_name = 'the bridge keeper'
favorite_color1 = 'blue'

# store user name and favorite color
user_name = input('What is your name?: ')
quest = input('what is your quest?: ')
favorite_color2 = input ('What is your favorite color?: ')

# reply with the end of the story
print('Well,', user_name, 'as you seek your quest of', quest, '- I am', programmer_name,
      'and', favorite_color1, 'is my favorite color.')
print('So off you go.')
