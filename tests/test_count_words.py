from lib.count_words import count_words

def test_returns_zero_for_empty_string():
    result = count_words("")

    assert result == 0

def test_returns_correct_number_of_words_for_three_word_string():
    result = count_words("One Two Three")

    assert result == 3

def test_punction_not_seperated_by_space_counts_as_part_of_word():
    result = count_words("One, Two, Three")

    assert result == 3

def test_words_not_seperated_by_space_count_as_one_word():
    result = count_words("One,Two,Three")

    assert result == 1