#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr@uw.edu)
Date: 08/10/2018

    Create a function that allows you to pull out a tag (passed as an argument to your function)
    from any URL (also passed as an argument to your function)
    Create a function to format the output in a meaningful way
    Create a function to write the formatted results to a txt file
    Upload your script and output file to canvas for full credit

"""
import requests


# get user input for a url and return it
def get_user_input():
    url = input(str('What URL?: '))
    response = requests.get(url)
    content = response.content
    return (url)


# get a tag from a url and return the result set of tags
def pull_out_tag():
    tag = input(str('What tag you would like pulled?: '))

    for line in lines:
        a_tag = line.find(tag)
        if a_tag is not None:
            print(a_tag.attrs['href'])

    return


response = requests.get(url)
content = response.content
print(content)

"""
response = requests.get(url)
dir(response)

lines = response.find_all(tag)

print(lines)
for line in lines:
    a_tag = line.find(tag)
    if a_tag is not None:
        print(a_tag.attrs['href'])
"""


# format the tag information
def meaningful_format(results):
    pass


#    soup = BeautifulSoup(content, 'lxml')


# write the data to a file
def write_to_file(filename, output):
    pass

# if __name__ == "__main__":
# for testing - in reality get user input
# url = "https://en.wikipedia.org/wiki/List_of_cities_in_Canada"
# real code
# url = get_user_input()
# tag = "a"
# call the pull_out_tag function to use soup to find all of the tags
# contents = pull_out_tag(url, tag)

# call the meaningful format function

# call the write to file function
