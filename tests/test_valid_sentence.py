import pytest
from lib.valid_sentence import valid_sentence

"""
Given an empty string return raise an error
"""
def test_raises_error_given_empty_string():
    with pytest.raises(Exception) as error:
        result = valid_sentence("")
    
    error_message = str(error.value)
    assert error_message == "Empty string given."

"""
Given valid sentence
(Valid = capital letter at start and a 
sentence ending punction at end, ?!.)
It returns True
"""
def test_returns_true_given_valid_sentence():
    result = valid_sentence("Hello world!")
    
    assert result == True

"""
Given an invalid sentence with no ending punction
It returns False
"""
def test_returns_false_given_no_ending_punction():
    result = valid_sentence("Hello world")
    
    assert result == False

"""
Given an invalid sentence with no capital letter at start
It returns False
"""
def test_returns_false_given_no_capital_letter_at_start():
    result = valid_sentence("hello world!")
    
    assert result == False

"""
Given a None value
It throws an error
"""
def test_raises_error_given_None_value():
    with pytest.raises(Exception) as error:
        result = valid_sentence(None)
    
    error_message = str(error.value)
    assert error_message == "valid_sentence expects str, given <class 'NoneType'>"

"""
Given a Int value
It throws an error
"""
def test_raises_error_given_an_int():
    with pytest.raises(Exception) as error:
        result = valid_sentence(1)
    
    error_message = str(error.value)
    assert error_message == "valid_sentence expects str, given <class 'int'>"