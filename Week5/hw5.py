#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 08/01/2018

"""

# file

# handle the file
myfilehandle = open("land_time_forgot.txt", 'r')

# convert the file handle to a list
mylist = myfilehandle.readlines()

# set counting variables
words = []
word_counts = {}
minwordlist = []

# calculate the total words
for line in mylist:
    linewords = line.split(' ')
    for innerword in linewords:
        words.append(innerword)

# calculate the unique words
for indwords in words:
    if indwords in word_counts:
        word_counts[indwords] = word_counts[indwords] + 1
    else:
        word_counts[indwords] = 1

# print out the outcome from counts
print('There are {} words'.format(len(words)), 'and {} unique words.'.format(len(set(words))))

# insert values into variables for total and total unique
totalwords = (len(words))
totaluniquewords = (len(set(words)))

# max word count calculation
max_value = max(word_counts.values())
max_key = max(word_counts, key=word_counts.get)

# print out the max key and value
print('The maximum word is {} with a count of {}.'.format(max_key.upper(), max_value))

# determine minimum word and word count
minwordlist = []
word_list = list(word_counts.items())
wordvalues = list(word_counts.values())
minwordvalue = min(wordvalues)
minwordcount = 0

for a, b in word_list:
    if b == minwordvalue:
        minwordlist.append(a)
        minwordcount = minwordcount + 1

print('The minimum word count is {} and the number of words with that count is {}.'.format(minwordvalue, minwordcount))

# determine percentages
totalpercentagewords = ((totaluniquewords / totalwords) * 100)
print('The percentage of words that are unique in the book is {:.1f}%.'.format(totalpercentagewords))
