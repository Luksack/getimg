from profanity import profanity
import os


def profane_words():
    project_dir = os.path.dirname(os.path.dirname(__file__))
    bad_words_location = os.path.join(project_dir, 'data', 'bad_words.txt')
    with open(bad_words_location) as input_file:
        bad_list = [line.strip() for line in input_file]

    # return bad_list
    print(bad_words_location)

def verify_nice(word):
    profanity.load_words(profane_words())
    words = word.replace(' ', '')
    if not words.isalpha():
        raise Exception('Input can contain only letters')
    if profanity.contains_profanity(word):
        raise Exception('Input should not be a profanity')

    # This is just placeholder to add any function later
    print('word is ok')

#
# if __name__ == '__main__':
#     verify_nice('dou')
