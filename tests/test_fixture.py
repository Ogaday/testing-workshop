from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    name: str
    dob: date


def greet(user: User):
    return f"Hello, {user.name}!"


import pytest


@pytest.fixture
def user() -> User:
    user = User(name="Harry Potter", dob=date(1980, 7, 31))
    return user


def test_greet(user):
    expected_greeting = "Hello, Harry Potter!"
    greeting = greet(user)
    assert greeting == expected_greeting
