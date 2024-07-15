import pytest


class ScreamError(Exception):
    """Raised for tantrums."""


def tantrum() -> None:
    """Throw a tantrum.

    Raises:
        ScreamError
    """
    raise ScreamError("Throwing a tantrum!")


def test_tantrum():
    with pytest.raises(ScreamError):
        tantrum()


def meditate() -> None:
    """Do nothing"""
    pass


@pytest.mark.xfail
def test_meditate():
    with pytest.raises(ScreamError):
        meditate()
