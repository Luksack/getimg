from profanity import profanity
import os


def profane_words():
    current_file = os.path.abspath(os.path.dirname(__file__))
    bad_words = os.path.join(current_file, 'data', 'bad_words.txt')
    with open(bad_words) as input_file:
        bad_list = [line.strip() for line in input_file]

    return bad_list


def verify_nice(word):
    profanity.load_words(profane_words())
    words = word.replace(' ', '')
    if not words.isalpha():
        raise Exception('Input can contain only letters')
    if profanity.contains_profanity(word):
        raise Exception('Input should not be a profanity')

    # This is just placeholder to add any function later
    print('word is ok')
