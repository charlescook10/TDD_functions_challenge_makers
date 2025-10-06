# Valid Sentence Function Design Recipe

## 1. Describe the Problem

>As a user
>So that I can improve my grammar
>I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def estimate_reading_time(text):
    """validates if a given sentence is valid. Meaning it starts with a capital letter and ends with a suitable sentence ending punctuation mark.

    Parameters: (list all parameters and their types)
        sentence: a string of words (e.g. "Hello, my name is Charles.")

    Returns: (state the return value and its type)
        a boolean true if the sentence is valid or false (e.g. True)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string return raise an error
"""
valid_sentence("") => throws an error

"""
Given valid sentence
It returns True
"""
valid_sentence("Hello world!") => True

"""
Given an invalid sentence with no ending punction
It returns False
"""
valid_sentence("Hello") => False

"""
Given an invalid sentence with no capital letter at start
It returns False
"""
valid_sentence("hello!") => False

"""
Given a None value
It throws an error
"""
valid_sentence(None) throws an error

"""
Given a Int value
It throws an error
"""
valid_sentence(int) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.valid_sentence import valid_sentence

"""
Given an empty string return raise an error
"""
def test_raises_error_given_empty_string():
    with pytest.raises(Exception) as error:
        result = valid_sentence("")
    
    error_message = str(error.value)
    assert error_message == "Empty string given."

```

Ensure all test function names are unique, otherwise pytest will ignore them!