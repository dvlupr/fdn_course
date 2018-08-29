#!/usr/bin/env python

myfile = open("land_time_forgot.txt", 'r')

mylist = myfile.readlines()
words = []

for line in mylist:
    linewords = line.split(' ')
    for innerword in linewords:
        words.append(innerword)

print('There are {} words'.format(len(words)))

firstline = mylist[0]
print(firstline)

project_title, author = firstline.split(', by')
project = project_title.split()

print('Project Title: ', project_title)
print('Author: ', author)

print('Project: ', project)
print('The author is: {}, the book is: {}, and the project is: {}.'.format(author, project_title, project))
