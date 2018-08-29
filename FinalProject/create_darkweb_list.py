#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 08/29/2018

Description:
Create a list of darkweb numbers (fictitious numbers).

"""
# import libraries
import os
import csv
import sys


# check to see if running on windows
if os.name is not "nt":
    print('stop process')
    sys.exit()
else:
    print('system ready...')


# functions
def fn_checkforfolder(d1):
    if folder in d1:
        return True
    else:
        return False

def fn_checkforfile(f1):
    if file in f1:
        return True
    else:
        return False


# create the directory for the list
cwd = os.getcwd()
os.chdir("C:\\")
directory = os.listdir()
folder = 'darkweb_process'

if fn_checkforfolder(directory) is True:
    print('directory exists...')
    os.chdir('C:\\darkweb_process')
    cwd = os.getcwd()
    print('current working directory is {}'.format(cwd))
elif fn_checkforfolder(directory) is False:
    print('directory does not exist...')
    print('creating directory...')
    os.chdir("C:\\")
    os.mkdir('darkweb_process')
    os.chdir('C:\\darkweb_process')
    cwd = os.getcwd()
    print('current working directory is {}'.format(cwd))
else:
    print('catastrophic failure big time')


# create list and assign seed mastercard numbers (fake for testing)
mastercard_list = []
mc_num = 5555555555000000


# create the number list
counter = 0
max_counter = 50
while counter < max_counter:
    counter = counter + 1
    mc_num = mc_num + 27
    mastercard_list.append('{}'.format(mc_num))


# alternate list
alternate_list = []
alt_num = 4111111111111111


# create the number list
counter = 0
max_counter = 25
while counter < max_counter:
    counter = counter + 1
    alt_num = alt_num + 83
    alternate_list.append('{}'.format(alt_num))

total_list = mastercard_list + alternate_list


# check to see if the file is there
cwd = os.getcwd()
os.chdir("C:\\darkweb_process")
directory2 = os.listdir()
file = 'darkweb.csv'

if fn_checkforfile(directory2) is True:
    print('file exists...')
    print('deleting old file...')
    os.chdir('C:\\darkweb_process')
    os.remove(file)
    cwd = os.getcwd()
    print('folder ready for the new file.')
elif fn_checkforfile(directory) is False:
    print('file does not exist...')
    cwd = os.getcwd()
else:
    print('catastrophic failure big time')

print('generating the new file...')


# write the list to a csv file
with open('darkweb.csv', 'w') as dw_file:
    writer = csv.writer(dw_file)
    writer.writerow(total_list)


# communicate the file disposition
cwd = os.getcwd()
path = os.listdir(cwd)

if file in path:
    print('file generated successfully!')
else:
    print('issue detected, troubleshooting required.')
