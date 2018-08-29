"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 6/27/2018

Creates variables to store user input for:
- User name
- User phone number
- Favorite cheese
- Average monthly amount spent on their favorite cheese

Calculates the daily amount this user spends on cheese and store this value as a variable
Uses the string split() method to store the last four digits of the user's phone number as a variable
Uses the string slicing method to store the first three letters of the user's name as a variable
Combines the phone number and username variables to create an account ID
Uses the replace() method to replace the first letter of your User ID with a Z and store that value as the final user ID
Prints a sentence that references the user ID, their favorite cheese and how much they spend each day on that cheese.
You may use any formatting method you prefer.
"""

# user input for four main variables
user_name = str(input('what is your name? : '))
user_phone = str(input('what is your phone number (###-####)? : '))
favorite_cheese = input('what is your favorite cheese? : ')
average_cheesespend = int(input('what is your monthly cheese spend? : '))

# create predicates
month_count = 30

daily_spend = average_cheesespend/month_count

last4 = user_phone.split('-')
last_four = last4[1]


# format output
print('-----')
print('daily spend:', daily_spend)

print('last four:', last_four)

print('first three:', user_name[0:3])

user_id = str(last_four + user_name[0:3])
print('user ID: ', user_id)

final_user_id = user_id.replace(user_id[4], 'z')

print('final user id: ', final_user_id)
print('------')
print('hello, ' + user_id + ' your favorite cheese is ' + favorite_cheese + ' and you spend $'
      + str(daily_spend) + ' each day on cheese.')


