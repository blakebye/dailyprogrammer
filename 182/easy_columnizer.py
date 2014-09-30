"""
This module takes a document in bulk and attempts to rewrite it
into columns based on what the user would like.
"""

import math

INPUT_FILE = "c182e-input.txt"


def line_to_lines(line, width):
    """
    This function takes one line of text, breaks it into words, and
    fills new lines that will take exactly "width" from as many words
    as possible and then pad with spaces to match width.
    """
    list_of_lines = list()
    words = line.split()
    if len(line) > width:
        # offsets the added +1 from the last space
        line_length = -1
        this_line = str()
        for word in words:
            line_length += len(word) + 1
            # there is space for that word in this line
            if line_length < width:
                this_line += str(word) + " "
            # there is not space
            else:
                # take back the last word, not putting it here
                line_length -= (len(word) + 1)
                # fill out the width with spaces
                while line_length < width:
                    this_line += " "
                    line_length += 1
                # put the line we've been working on in the list
                list_of_lines.append(this_line)
                # start a new line with the word we're on
                this_line = str(word) + " "
                line_length = len(word)
        while line_length < width:
            this_line += " "
            line_length += 1
        list_of_lines.append(this_line)
    # extra spaces are consistent at the end of lines, too lazy to find why
    list_of_lines = ["".join(list(line)[:-2]) for line in list_of_lines]
    return list_of_lines


def columnize(inp):
    """
    This funcion takes a filename and works it's columnizing magic.
    """
    # the first line is always the configuration for the layout
    number, width, space = [int(x) for x in inp.readline().split()]
    # this will become a list of lines of proper width
    list_of_lines = list()
    for line in inp:
        list_of_lines.extend(line_to_lines(line, width))
    # this ensures the columns are of similar lengths and not cut-off
    max_rows = int(math.ceil(len(list_of_lines) / float(number)))
    # this will be our text in columns
    columns = list()
    for old_location, line in enumerate(list_of_lines):
        if old_location < max_rows:
            # just move over the first column
            columns.append(line)
        else:
            # these columns are shifted up and spaced appropriately
            new_location = old_location % max_rows
            columns[new_location] += " " * space + str(line)
    return columns


def main():
    """
    This function displays the solution for Lorem ipsum
    """
    inp = open(INPUT_FILE)
    columns = columnize(inp)
    for column in columns:
        print column

if __name__ == "__main__":
    main()
