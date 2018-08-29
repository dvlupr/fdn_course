#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 07/25/2018
"""

myfile = open("land_time_forgot.txt", 'r')

mylist = myfile.readlines()
mythird = int(len(mylist) / 3)

myfirstthird = mylist[0:mythird]
mysecondthird = mylist[mythird:(mythird * 2)]
mythirdthird = mylist[(mythird * 2):(len(mylist))]

print('There are approximately', len(mylist), 'lines in this file.')
print('One third: ', mythird)
print('-----')
print('Second third: ', mysecondthird)
print('Last line in first third: ', myfirstthird[-1])
print('Last line in second third: ', mysecondthird[1:])
print('----')

with open('outfile.txt', 'w')as outfh:
    outfh.write(myfirstthird[-1])
    outfh.write(mysecondthird[-1])
