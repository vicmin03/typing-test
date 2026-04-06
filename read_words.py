import random


def read_words(n):
    # params:
    #   n (int): the number of words to be returned
    # returns:
    #   list of n words of length 3 chars or more

    with open("basic_english_2000.txt") as file:
        # read each line in file (includes linebreak '\n')
        all_words = file.readlines()
        valid_words = [x.rstrip('\n') for x in all_words if len(x) >= 5]

        return random.sample(valid_words, n)
