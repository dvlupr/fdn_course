#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 07/01/2018
"""


# functions
def fn_convertdollar(d1):
    return'${:,.2f}'.format(d1)


def fn_salestax(t1):
    return t1 * tax_rate


def fn_convertfloat(f1):
    return float(f1)


# predicates
tax_rate = .101
license_fee = 50.00
dealer_prep = 50.00


# user form
pur_name = str(input("what is your name?: "))
pur_address = str(input('what is your address?: '))
pur_phone = str(input('what is your phone number (###-###-####)?: '))
car_make = input('what is the car make?: ')
car_model = input('what is the car model?: ')
pur_price = input('what is the car purchase price?: ')


# calculations
sales_tax = fn_salestax(fn_convertfloat(pur_price))
total_price = (fn_convertfloat(pur_price) + sales_tax + license_fee + dealer_prep)


# build up the customer number
last_four = pur_name[-4:]
underscore = '_'
area_code = pur_phone.split('-')
namac = last_four + underscore + area_code[0]


# print the output for the assignment.
print('\n-----')
print('Hello {}!'.format(pur_name.title()))
print('\nThank you for your purchase of a {} {}.\n'.format(car_make.capitalize(), car_model.capitalize()))
print('The following is a breakdown of your total price: \n')
print('Sales Price: {}'.format(fn_convertdollar(fn_convertfloat(pur_price))))
print('Tax: {}'.format(fn_convertdollar(sales_tax)))
print('License Fee: {}'.format(fn_convertdollar(license_fee)))
print('Dealer Prep: {}'.format(fn_convertdollar(dealer_prep)))
print('Total Price: {}'.format(fn_convertdollar(total_price)))
print('\nYou have been assigned an ID number of {}.'.format(namac.upper()))
print('\nPlease refer to your ID number if you have any questions.')
print('\nSincerely, ')
print('\nThe Management')
print('-----')
