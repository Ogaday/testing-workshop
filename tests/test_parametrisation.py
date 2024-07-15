import pytest


def mul(a: float, b: float) -> float:
    """Multiply two numbers

    Args:
        a: First factor
        b: Second factor

    Returns:
        product: float
    """
    return a * b


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 2, 4),
        (1, 2, 2),
        (-1, 2, -2),
    ],
)
def test_mul(a, b, expected):
    assert mul(a, b) == expected
