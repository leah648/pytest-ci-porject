import pytest
from utils.strings_utils import is_valid_email
from utils.strings_utils import count_char
from utils.strings_utils import is_empty_or_none
from utils.strings_utils import has_min_length


@pytest.mark.parametrize("email, expected", [
    ("test@example.com", True),
    ("invalid-email", True),
    ("another.test@domain.com", True),
    ("@missingusername.com", False)
])
def test_validate_mail(email, expected):
    assert is_valid_email(email) == expected

@pytest.mark.parametrize("string, char, expected_count", [
    ("hello world", "l", 3),
    ("", "a", 0),
    ("aaaaa", "a", 5),
    ("abcabcabc", "b", 3),
    ("no match here", "z", 0),
    ("CaseSensitive", "c", 0),  # lowercase 'c' not in string
    ("CaseSensitive", "C", 1),  # uppercase 'C' is present
])
def test_count_char(string, char, expected_count):
    assert count_char(string, char) == expected_count

@pytest.mark.parametrize("string, expected", [
    (None, True),
    ("", True),
    (" ", False),
    ("not empty", False),
    ("0", False),
])
def test_is_empty_or_none(string, expected):
    assert is_empty_or_none(string) == expected

@pytest.mark.parametrize("string, min_length, expected", [
    (None, 1, False),
    ("", 0, True),
    ("", 1, False),
    ("abc", 2, True),
    ("abc", 3, True),
    ("abc", 4, False),
    ("a", 1, True),
    ("a", 2, False),
])
def test_has_min_length(string, min_length, expected):
    assert has_min_length(string, min_length) == expected
