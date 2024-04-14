import pytest


@pytest.fixture
def json_res():
    f = open('tests/fixtures/result.txt', 'r')
    return f.read()