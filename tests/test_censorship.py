from censorship import is_nice

good_word = 'cat'
curse_word = 'pussy'
not_alpha = 'hey!@#123'
good_with_spaces = 'husky dog'
bad_with_spaces = 'husky dog 1'
curse_word_with_spaces = 'fuck you'


def test_correct_word(capfd):
    is_nice(good_word)

    out, err = capfd.readouterr()
    assert out.strip() == 'word is ok'


def test_bad_word(capfd):
    is_nice(curse_word)

    out, err = capfd.readouterr()
    assert out.strip() == 'Err: contains profanity: %s' % curse_word


def test_not_alpha(capfd):
    is_nice(not_alpha)

    out, err = capfd.readouterr()
    assert out.strip() == 'Input can contain only letters'


def test_spaces(capfd):
    is_nice(good_with_spaces)

    out, err = capfd.readouterr()
    assert out.strip() == 'word is ok'


def test_spaces_bad(capfd):
    is_nice(bad_with_spaces)

    out, err = capfd.readouterr()
    assert out.strip() == 'Input can contain only letters'


def test_spaces_curse(capfd):
    is_nice(curse_word_with_spaces)

    out, err = capfd.readouterr()
    assert out.strip() == 'Err: contains profanity: %s' % curse_word_with_spaces
