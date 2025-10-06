import pytest
from lib.estimate_reading_time import estimate_reading_time

"""
Given an empty string return 0
"""
def test_returns_zero_given_empty_string():
    result = estimate_reading_time("")

    assert result == 0

"""
Given 200 words
It returns 60 representing a minute
"""
def test_returns_60_given_200_words():
    string = ""
    for i in range(200):
        string += "Word "
    result = estimate_reading_time(string)

    assert result == 60

"""
Given at least a single word 
It returns at least 1 
"""
def test_returns_at_least_1_given_1_word():
    result = estimate_reading_time("word")

    assert result == 1

"""
Given a None value
It throws an error
"""
def test_returns_error_given_None_value():
    with pytest.raises(Exception) as error:
        result = estimate_reading_time(None)
    error_message = str(error.value)

    assert error_message == "estimate_reading_time expects str, given <class 'NoneType'>"

"""
Given a Int value
It throws an error
"""
def test_returns_error_given_Int_value():
    with pytest.raises(Exception) as error:
        result = estimate_reading_time(1)
    error_message = str(error.value)

    assert error_message == "estimate_reading_time expects str, given <class 'int'>"