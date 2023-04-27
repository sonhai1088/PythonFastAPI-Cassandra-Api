import pytest


def test_assert():
    assert True is True

def test_equal():
    assert 1 == 1

def test_equal():
    assert 1 != 1

def test_invalid_assert():
    with pytest.raises(AssertionError):
        assert True is not True
