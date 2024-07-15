from typing import Iterator
from unittest import TestCase


def fibonacci(n: int) -> Iterator[int]:
    """Iterate over the first n terms of the Fibonacci sequence.

    Args:
        n: The number of terms to iterate over

    Examples:
        >>> list(fibonacci(7))
        [1, 1, 2, 3, 5, 8, 13]
    """
    last, current = 0, 1
    for _ in range(n):
        yield current
        last, current = current, current + last


class TestFibonacci(TestCase):
    """Fibonacci test case."""

    def test_fibonacci(self):
        """Test fibonacci sequence works up to 7."""
        self.assertEqual(list(fibonacci(7)), [1, 1, 2, 3, 5, 8, 13])


def test_fibonacci():
    """Test fibonacci sequence works up to 7."""
    assert list(fibonacci(7)) == [1, 1, 2, 3, 5, 8, 13]
