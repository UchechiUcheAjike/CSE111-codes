from names import make_full_name, extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Kate", "Living") == "Living; Kate"
    assert make_full_name("Love", "Jha") == "Jha; Love"
    assert make_full_name("Kilimongo", "Zum-ona") == "Zum-ona; Kilimongo"


def test_extract_family_name():
    assert extract_family_name ("Living; Kate") == "Living"
    assert extract_family_name ("Jha; Love") == "Jha"
    assert extract_family_name ("Zum-ona; Kilimongo") == "Zum-ona"

def extract_given_name():
    assert extract_given_name ("Living; Kate") == "Kate"
    assert extract_given_name ("Jha; Love") == "Love"
    assert extract_given_name ("Zum-ona; Kilimongo") == "Kilimongo"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])
