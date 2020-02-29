"""wordtools: compute word statitics about a text file"""

def _clean_infile(infile):
    clean_words = []
    
    puncts = "!.,:;-?'\"\n"
    punct_table = str.maketrans(puncts, " "*len(puncts))
    
    for line in infile:
        # make all one case
        lower_line = line.lower()
        
        # remove punctuation
        clean_line = lower_line.translate(punct_table)
        
        # split into words
        clean_line_of_words = clean_line.split()
        
        clean_words = clean_words + clean_line_of_words
        
    return clean_words

def list_words_from_txt(txt_source):
    """Create a list of words from arbitrary text."""
    print(f"Reading from file: {txt_source}")
    with open(txt_source) as infile:
        word_list = _clean_infile(infile)
    return word_list

def write_words_to_txt(word_list, txt_destination):
    print(f"Output file is: {txt_destination}")
    with open(txt_destination, "w") as outfile:
        words = ("\n").join(word_list)
        outfile.write(words)
        outfile.write("\n")

def count_each_word(word_list):
    word_count_dict = {}
    for word in word_list:
        count = word_count_dict.setdefault(word, 0)
        count += 1
        word_count_dict[word] += 1
    return word_count_dict

def _sort_word_count_dict(word_count_dict):
    word_list = list(word_count_dict.items())
    word_list.sort(key=lambda x: x[1])
    return word_list


def print_common_words(word_count_dict):
    word_list = _sort_word_count_dict(word_count_dict)
    for word in reversed(word_list[-5:]):
        print(f"{word}")
    
def print_uncommon_words(word_count_dict):
    word_list = _sort_word_count_dict(word_count_dict)
    for word in (word_list[:5]):
        print(f"{word}")