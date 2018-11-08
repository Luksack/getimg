import pytest

from main.censorship import verify_nice

GOOD_WORD = 'cat'
CURSE_WORD = 'pussy'
NOT_ALPHA = 'hey!@#123'
GOOD_WITH_SPACES = 'husky dog'
BAD_WITH_SPACES = 'husky dog 1'
CURSE_WORD_WITH_SPACES = 'fuck you'
PROFANITY_EXCEPTION = 'Input should not be a profanity'
ONLY_LETTERS_EXCEPTION = 'Input can contain only letters'


def test_correct_word():
    verify_nice(GOOD_WORD)


def test_bad_word():
    with pytest.raises(Exception) as ex:
        verify_nice(CURSE_WORD)

    assert PROFANITY_EXCEPTION in str(ex.value)


def test_not_alpha():
    with pytest.raises(Exception) as ex:
        verify_nice(NOT_ALPHA)

    assert ONLY_LETTERS_EXCEPTION in str(ex.value)


def test_spaces():
    verify_nice(GOOD_WITH_SPACES)


def test_spaces_bad():
    with pytest.raises(Exception) as ex:
        verify_nice(BAD_WITH_SPACES)

    assert ONLY_LETTERS_EXCEPTION in str(ex.value)


def test_spaces_curse():
    with pytest.raises(Exception) as ex:
        verify_nice(CURSE_WORD_WITH_SPACES)

    assert PROFANITY_EXCEPTION in str(ex.value)
