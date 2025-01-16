import pytest
from src.palindrome import isPalindrome

@pytest.mark.parametrize(
    "num, result",
    [
        (454, True),         # Positive Case 1
        (0, True),           # Positive Case 2
        (2662, True),        # Positive Case 3
        (12321, True),       # Positive Case 4
        (987, False),        # Negative Case 1
        (10, False),         # Negative Case 2
        (12345, False),      # Negative Case 3
        (-454, False),       # Negative Case 4
    ],
)
def test_is_palindrome(num, result):
    assert isPalindrome(num) == result
