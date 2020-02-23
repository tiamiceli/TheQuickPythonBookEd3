#!/env python3

import string

""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""

puncts = "!.,:;-?'\"\n"
punct_table = str.maketrans(puncts, " "*len(puncts))

line_count = 0
word_count = 0
char_count = 0

with open('word_count.tst', 'r') as infile:
    for line in infile:
        line_count += 1
        char_count += len(line)
        for word in line.split():
            word_count += 1
            for char in word:
                if char in string.ascii_letters:
                    char_count += 1

# print the answers using the format() method
print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                               word_count, char_count))
    

