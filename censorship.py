from profanity import profanity


def is_nice(word):
    custom_bad_words = []
    with open('bad_words.txt') as inputfile:
        for line in inputfile:
            custom_bad_words.append(line.strip())
    profanity.load_words(custom_bad_words)
    words = word.replace(' ', '')
    if words.isalpha():
        print('good')
        if profanity.contains_profanity(word):
            print('Err: contains profanity: %s' % word)
        else:
            # This is just placeholder to add any function later
            print('word is ok')
    else:
        print('Input can contain only letters')
