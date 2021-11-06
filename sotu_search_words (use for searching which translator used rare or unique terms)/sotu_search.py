"""
This program enables users to find out in which SOTU addresses a particular word was used
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


# set up dictionary with words as keys, list of filenames as values for where those words show up
sotu_word_dict = {}

# read every text file in directory with prior collection
path = "state-of-the-union-corpus-1989-2017"

list_of_files = os.listdir(path)

for filename in list_of_files:
    # get set of words for filename
    word_set = get_word_set_from_file(path + "/" + filename)

    for a_word in word_set:
        if a_word in sotu_word_dict:
            # if the word is already in the dictionary
            sotu_word_dict[a_word] += [filename]
        else:
            sotu_word_dict[a_word] = [filename]

# inform user through a text user interface

user_asking = True

while user_asking:
    word_query = input("Enter word to search in SOTU addresses, or enter to exit: ")

    if word_query == '':
        # exit program
        user_asking = False
    elif word_query in sotu_word_dict:
        # inform user of SOTUs in which the word shows up
        print ("The word " + word_query + " is in the following SOTUs")
        for sotu in sotu_word_dict[word_query]:
            print(sotu)
        print()
    else:
        # the word is not in any SOTU
        print ("The word " + word_query + " is not in any SOTU.")
