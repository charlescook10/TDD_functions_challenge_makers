from lib.make_snippet import make_snippet

def test_given_empty_string_returns_empty_string():
    result = make_snippet("")

    assert result == ""

def test_returns_words():
    result = make_snippet("Dear Diary,")

    assert result == "Dear Diary,"

def test_returns_first_five_words_and_ellipsis():
    result = make_snippet("Dear Diary, today I learnt how to test")

    assert result == "Dear Diary, today I learnt..."