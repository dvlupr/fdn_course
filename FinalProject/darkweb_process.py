#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 08/29/2018

Description:
Read in files, compare darkweb numbers to the mastercard list, and
determine if any are on the main list.

"""
import csv
import os


# function to communicate the output files disposition
def fn_filesuccess(f1):
    cwd = os.getcwd()
    path = os.listdir(cwd)
    if file in path:
        print('file generated successfully!')
    else:
        print('issue detected, troubleshooting required.')
    return


# Get user input for the file locations (if the other processes are run, they will be in c:\darkweb_process
filename1 = input('what is the name and location of the Mastercard file to import? ')
filename2 = input('what is the name and location of the Darkweb file to import? ')
print('-----')


# using the csv reader, create the mastercard list
mc_list = []
with open(filename1, newline='') as mc:
    reader = csv.reader(mc)
    mc_list = list(reader)


# using the csv reader, create the darkweb list
dw_list = []
with open(filename2) as dw:
    reader2 = csv.reader(dw)
    dw_list = list(reader2)


# create the compromised and not compromised lists
compromised_list = []
not_listed = []


# loop through the darkweb file and capture any listed from the darkweb file
for card_num in dw_list[0]:
    if card_num in mc_list[0]:
        compromised_list.append(card_num)
        print('Compromised Number: {}'.format(card_num))
    elif card_num not in mc_list[0]:
        not_listed.append(card_num)
        print('Not Listed: {}'.format(card_num))
    else:
        print('troubleshoot')
print('-----')

# output file names
file = 'compromised_file.csv'
file2 = 'not_listed.csv'


# navigate to the proper cwd and create the output file of compromised numbers to revoke
os.chdir("C:\\darkweb_process")
cwd = os.getcwd()
print('Creating file at ', cwd)
with open(file, 'w') as cl_file:
    writer = csv.writer(cl_file)
    writer.writerow(compromised_list)
fn_filesuccess(file)
print('-----')


# navigate to the proper cwd and create the output file of darkweb numbers
os.chdir("C:\\darkweb_process")
cwd = os.getcwd()
print('Creating file at ', cwd)
with open(file2, 'w') as cl_file:
    writer = csv.writer(cl_file)
    writer.writerow(not_listed)
fn_filesuccess(file2)
print('-----')
