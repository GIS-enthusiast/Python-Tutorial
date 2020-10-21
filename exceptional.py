import sys
from math import log

DIGIT_MAP = {
    'eight': '8',
    'five': '5',
    'four': '4',
    'nice': '9',
    'one': '1',
    'seven': '7',
    'six': '6',
    'ten': '10',
    'three': '3',
    'two': '2',
    'zero': '0'
}

def convert(s):
    """Convert a string to an integer"""
    try:
        number = '' # Creates empty string
        for token in s:
            number += DIGIT_MAP[token] # Same as number = number + DIGIT_MAP[token]
        return int(number)
        
    except (KeyError, TypeError) as e: # e is the exception object.
        print(f'Conversion error: {e!r}', # ! after expression in f string object brings in information from the REPL.
        file=sys.stderr)
        pass # This is a no op. Allows us to have an empty block. Block can not be empty in Python.
    raise # Reraises the exception error on errors associated with string_log.

def string_log(s):
    v = convert(s)
    return log(v) # Compute natural log.
