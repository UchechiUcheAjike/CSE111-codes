from words import prefix, suffix
import pytest

def test_prefix_of_word():
    assert "words" == prefix("string1", "string2")
    assert "words" == prefix("string1", "string2")
