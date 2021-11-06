"""
This program identifies words in a particular text file that are not found in a separate collection of text files.
"""

# need to import os to access list of file
import os

def remove_characters(full_str, remove_chars):
    ' returns version of full_str without remove_chars '
    clean_str = full_str

    # go through each characater and remove it from the list
    for no_char in remove_chars:
        clean_str = clean_str.replace(no_char, '')

    # return clean string
    return clean_str


def get_word_set_from_file(filename):
    ' returns set of words in file '
    curr_file = open(filename)
    print("Processing " + filename)

    # read content
    curr_file_content = curr_file.read().lower()

    # we can close file since we no longer need it open
    curr_file.close()

    # get rid of punctuation and other unwanted characters
    curr_file_content_only_words = remove_characters(curr_file_content, '.,;!?:-\'"$0123456789')

    # return word list from the content with only words
    return set(curr_file_content_only_words.split())


# populate a set with all words used in prior collection
prior_words = set()

# read every text file in directory with prior collection
path = "state-of-the-union-corpus-1989-2017"

list_of_files = os.listdir(path)

for filename in list_of_files:
    # get set of words for filename
    word_set = get_word_set_from_file(path + "/" + filename)

    # augment prior_words set by adding the words from filename
    prior_words = prior_words | word_set
    

# populate a set with all words used in new text file
filename = "Trump_2019.txt"

new_words = get_word_set_from_file(filename)

# subtract prior set from new set
never_used_before_words = new_words - prior_words

# inform user about words previously not used that were used in the new text file
for a_word in never_used_before_words:
    print(a_word, end=", ")
