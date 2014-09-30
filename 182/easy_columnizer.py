"""
This module takes a document in bulk and attempts to rewrite it
into columns based on what the user would like.
"""

import math
import sys

def get_file():
    if len(sys.argv) == 2:
        f = open(sys.argv[1])
    else:
        print "easy_columnizer.py: no file given to columnize"
        f = raw_input("What is the name of the file you wish to columnize?\n")
        f = open(f)
    return f

def columnize():
    f = get_file()
    number, width, space = [int(x) for x in f.readline().split()]
    list_of_lines = list()
    for line in f:
        words = line.split()
        if len(line) > width:
            line_length = -1 # offsets the added +1 from the last space
            this_line = str()
            for word in words:
                line_length += len(word) + 1
                # there is space for that word in this line
                if line_length <= width:
                    this_line += str(word) + " "
                # there is not space
                else:
                    # take back the last word, not putting it here
                    line_length -= (len(word) + 1)
                    # fill out the width with spaces
                    while line_length < (width + space):
                        this_line += " "
                        line_length += 1
                    # put the line we've been working on in the list
                    list_of_lines.append(this_line)
                    # start a new line with the word we're on
                    this_line = str(word) + " "
                    line_length = len(word)
            while line_length < (width + space):
                        this_line += " "
                        line_length += 1
            list_of_lines.append(this_line)
    list_of_lines = [''.join(list(line)[:-1]) for line in list_of_lines]
    # list_of_lines is missing last line
    max_rows = int(math.ceil(len(list_of_lines) / float(number)))
    # row length is perfect, no lines cut off
    new_list = list()
    # our new ROW LIST is empty
    for old_location, line in enumerate(list_of_lines):
        if old_location < max_rows:
            new_list.append(line)
        else:
            new_location = old_location % max_rows
            new_list[new_location] += " " + str(line)
    for line in new_list:
        print line

columnize()
