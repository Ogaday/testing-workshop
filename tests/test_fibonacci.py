from typing import Iterator


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
