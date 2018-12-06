import pytest

from resources.censorship import verify_nice

GOOD_WORD = 'cat'
CURSE_WORD = 'pussy'
NOT_ALPHA = 'hey!@#123'
BAD_WITH_SPACES = 'husky dog 1'
MULTI_LETTERS = 'coooockkkkk'
PROFANITY_EXCEPTION = 'Input should not be a profanity'
ONLY_LETTERS_EXCEPTION = 'Input can contain only letters'
NO_QUERY = ''


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
    with pytest.raises(Exception) as ex:
        verify_nice(BAD_WITH_SPACES)

    assert ONLY_LETTERS_EXCEPTION in str(ex.value)


def test_multi_letters():
    with pytest.raises(Exception) as ex:
        verify_nice(MULTI_LETTERS)

    assert PROFANITY_EXCEPTION in str(ex.value)


def test_no_query():
    with pytest.raises(IndexError) as ex:
        verify_nice(NO_QUERY)

    assert 'string index out of range' in str(ex.value)
