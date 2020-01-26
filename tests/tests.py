import pytest

from data import clean


def test_clean():
    plot = "Hello\r\nWorld\'[1]"
    assert clean(plot) == "Hello World"


