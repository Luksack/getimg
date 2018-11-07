from profanity import profanity
import os


def is_nice(word):
    custom_bad_words = []
    current_file = os.path.abspath(os.path.dirname(__file__))
    bad_words = os.path.join(current_file, './data/bad_words.txt')
    with open(bad_words) as input_file:
        for line in input_file:
            custom_bad_words.append(line.strip())
    profanity.load_words(custom_bad_words)
    words = word.replace(' ', '')
    if words.isalpha():
        if profanity.contains_profanity(word):
            print('Err: contains profanity: %s' % word)
        else:
            # This is just placeholder to add any function later
            print('word is ok')
    else:
        print('Input can contain only letters')
