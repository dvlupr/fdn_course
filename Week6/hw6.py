#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 08/07/2018
"""


# file placed at in project
# jenkins.csv
# 24,3


# functions
def fn_numberofpizza(p1, p2):
    return (p1 * p2)


def fn_totalpizzas(pt1, pt2):
    return pt1 / pt2


def fn_pizzasubtotal(pst1):
    return pst1 * pizza_cost


def fn_pizzatotal(pz1):
    return pz1 + float(fn_salestax(pizza_subtotal)) + float(fn_tiprate(pizza_subtotal)) + delivery_fee


def fn_costperperson(cp1, cp2):
    return fn_convertdollar(cp1 / cp2)


def fn_convertdollar(d1):
    return '${:,.2f}'.format(d1)


def fn_salestax(t1):
    return t1 * tax_rate


def fn_tiprate(tp1):
    return tp1 * tip_rate


def fn_convertfloat(cf1):
    return float(cf1)


def fn_leftoverslices():
    return int((total_pizzas * avg_slices) % total_slices)


# fixed variables
pizza_cost = 15.99
total_slices = 8
tax_rate = .101
tip_rate = .18
delivery_fee = 3.99
people_num = 0
avg_slices = 0

# user input
input_type = input('Do you have a .csv with people and slices (format: people, slices) to upload?(y/n): ')
if input_type.lower() == 'y':
    file_location = str(input('What is the name of your file? (include .csv): '))
    myfilehandle = open("jenkins.csv", 'r')
    raw_ordername = myfilehandle.name
    ordername = (raw_ordername.split('.csv'))
    raw_orderkey = ordername[0]
    orderkey = raw_orderkey
    myorder = myfilehandle.readlines()
    newlist = []
    for value in myorder:
        value = value.split(",")
        newlist.extend(value)
    people_num = int(newlist[0])
    avg_slices = int(newlist[1])
elif input_type.lower() == 'n':
    people_num = int(input('How many people want pizza?: '))
    avg_slices = int(input('What is the average number of slices per person?: '))
else:
    print('no input detected - terminating program')

# how many pizzas to order based on number of people and average number of slices
order_num = fn_numberofpizza(people_num, avg_slices)
total_pizzas = fn_totalpizzas(order_num, total_slices)
pizza_subtotal = fn_pizzasubtotal(total_pizzas)
pizza_total = fn_pizzatotal(pizza_subtotal)

# output
print('-----')
print('You need {} pizzas.'.format(int(total_pizzas)))
print('The total cost is {}.\n'.format(fn_convertdollar(pizza_total)))
print('There will be {} leftover slices.\n'.format(fn_leftoverslices()))
print('Each person owes {}.'.format(fn_costperperson(pizza_total, people_num)))
print('-----')
