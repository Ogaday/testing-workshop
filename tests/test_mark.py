import pytest


def test_true():
    assert True


@pytest.mark.skip
def test_skip():
    raise Exception("I never get called")


@pytest.mark.xfail
def test_xfail():
    assert False


from time import sleep


@pytest.mark.slow
def test_slow():
    sleep(1)
    assert True
