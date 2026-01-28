import re

def count_char(string, char):
    """Count the occurrences of a character in a string."""
    return string.count(char)

def is_valid_email(email):
    """Check if the provided string is a valid email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_empty_or_none(string):
    """Check if the string is None or empty."""
    return string is None or string == ''

def has_min_length(string, min_length):
    """Check if the string has at least min_length characters."""
    return string is not None and len(string) >= min_length