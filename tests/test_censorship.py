import pytest

from main.censorship import verify_nice

good_word = 'cat'
curse_word = 'pussy'
not_alpha = 'hey!@#123'
good_with_spaces = 'husky dog'
bad_with_spaces = 'husky dog 1'
curse_word_with_spaces = 'fuck you'


def test_correct_word():
    verify_nice(good_word)


def test_bad_word():
    with pytest.raises(Exception) as ex:
        verify_nice(curse_word)

    assert 'Input should not be a profanity' in str(ex.value)


def test_not_alpha():
    with pytest.raises(Exception) as ex:
        verify_nice(not_alpha)

    assert 'Input can contain only letters' in str(ex.value)


def test_spaces():
    verify_nice(good_with_spaces)


def test_spaces_bad():
    with pytest.raises(Exception) as ex:
        verify_nice(bad_with_spaces)

    assert 'Input can contain only letters' in str(ex.value)

def test_spaces_curse():
    with pytest.raises(Exception) as ex:
        verify_nice(curse_word_with_spaces)

    assert 'Input should not be a profanity' in str(ex.value)