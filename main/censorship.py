from profanity import profanity
import os


def profane_words():
    project_dir = os.path.dirname(os.path.dirname(__file__))
    bad_words_location = os.path.join(project_dir, 'data', 'bad_words.txt')
    with open(bad_words_location) as input_file:
        bad_list = [line.strip() for line in input_file]

    return bad_list


def remove_duplicates(word):
    cleared_chars = []

    for i in range(len(word)):
        if i == 0:
            cleared_chars += word[0]
        else:
            if word[i] not in cleared_chars[-1]:
                cleared_chars += word[i]
    new_word = ("".join(cleared_chars))
    return new_word


def verify_nice(word):
    profanity.load_words(profane_words())
    clear_word = remove_duplicates(word)
    print(clear_word)
    # Radek said 'only keywords no spaces allowed'
    if not word.isalpha():
        raise Exception('Input can contain only letters')
    if profanity.contains_profanity(word):
        raise Exception('Input should not be a profanity')
    if profanity.contains_profanity(clear_word):
        raise Exception('Input should not be a profanity duplicates')


