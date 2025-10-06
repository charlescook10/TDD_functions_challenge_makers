# Estimate Reading Time Function Design Recipe

## 1. Describe the Problem

>As a user
>So that I can manage my time
>I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def estimate_reading_time(text):
    """estimates the time needed to read a string assuming 200 words can be read in a minute

    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a integer representing the seconds needed to read the text (e.g. 60)

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
Given an empty string return 0
"""
estimate_reading_time("") => 0

"""
Given 200 words
It returns 60 representing a minute
"""
estimate_reading_time("Hello world... up to 200 words") => 60

"""
Given at least a single word 
It returns at least 1 
"""
extract_uppercase("hello!") => 1

"""
Given a None value
It throws an error
"""
estimate_reading_time(None) throws an error

"""
Given a Int value
It throws an error
"""
estimate_reading_time(int) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.estimate_reading_time import estimate_reading_time

"""
Given an empty string return 0
"""
def test_returns_zero_given_empty_string():
    result = estimate_reading_time("")

    assert result == 0
```

Ensure all test function names are unique, otherwise pytest will ignore them!