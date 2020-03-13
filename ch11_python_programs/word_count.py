#!/opt/anaconda3/bin/python3
""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""

from argparse import ArgumentParser

def wc(filename, request_lines=False, request_words=False, request_chars=False):
    # open the file
    infile = open(filename)
    # read the file and split into lines
    lines = infile.read().split("\n")

    # get number of lines with len() function
    line_count = len(lines)
    
    if request_lines:
        print(f"File has {line_count} lines")
    
    # initialize other counts
    word_count = 0
    char_count = 0

    # iterate through the lines
    for line in lines:
        # split into words
        words = line.split()
        word_count += len(words)
        # len() function returns characters when used on a string
        char_count += len(line)

    if request_words:
        print(f"File has {word_count} words")
        
    if request_chars:
        print(f"File has {char_count} chars")
    
def main():
    ap = ArgumentParser()
    ap.add_argument("-l", "--line",
            action="store_true", dest="request_lines", default=False,
            help="return number of lines")
    ap.add_argument("-w", "--word",
            action="store_true", dest="request_words", default=False,
            help="return number of words")
    ap.add_argument("-c", "--characters",
            action="store_true", dest="request_chars", default=False,
            help="return number of chars")
    ap.add_argument("-f", "--file", dest="filename",
            help="file input")
    
    args = ap.parse_args()
    
    if (args.request_lines or args.request_words or args.request_chars) == False:
        args.request_lines = args.request_words = args.request_chars = True
    
    if args.filename == None:
        print("Please provide an input file with option -f")
        
    
    wc(args.filename, args.request_lines, args.request_words, args.request_chars)
    
if __name__ == '__main__':
    print("running as a script")
    main()
else:
    print("loaded as a module")
