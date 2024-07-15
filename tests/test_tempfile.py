import tempfile
from pathlib import Path

import pytest


def save_file(filepath: str, contents: str):
    """Save a string to a filepath."""
    with open(filepath, "w") as f:
        f.write(contents)


@pytest.fixture
def directory():
    with tempfile.TemporaryDirectory() as dir:
        # Note the yield here instead of return:
        yield dir


def test_save_file(directory):
    # Arange
    contents = "Hello, world!\n"
    filepath = Path(directory) / "test.txt"

    # Act
    save_file(filepath=filepath, contents=contents)

    # Assert
    with open(filepath) as f:
        assert f.read() == contents
