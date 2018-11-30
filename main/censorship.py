from profanity import profanity
import os


def profane_words():
    project_dir = os.path.dirname(os.path.dirname(__file__))
    bad_words_location = os.path.join(project_dir, 'data', 'bad_words.txt')
    with open(bad_words_location) as input_file:
        bad_list = [line.strip() for line in input_file]

    return bad_list


def remove_duplicates(word):
    cleared_word = word[0]

    for i in range(len(word)):
        if word[i] != cleared_word[-1]:
            cleared_word += word[i]

    return cleared_word


def verify_nice(word):
    profanity.load_words(profane_words())
    clear_word = remove_duplicates(word)
    if not word.isalpha():
        raise Exception('Input can contain only letters')
    if any([w for w in [word, clear_word] if profanity.contains_profanity(w)]):
        raise Exception('Input should not be a profanity')
