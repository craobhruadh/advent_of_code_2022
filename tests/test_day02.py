import pytest
from solutions.day_02 import read_file, problem_one, problem_two


def test_read_file():
    data = read_file('./tests/data/day02_test.txt')
    assert data[0][0] == 'A'
    assert data[0][1] == 'Y'
    assert data[-1][0] == 'C'
    assert data[-1][1] == 'Z'


def test_problem_one():
    data = read_file('./tests/data/day02_test.txt')
    assert problem_one(data) == 15


def test_problem_two():
    data = read_file('./tests/data/day02_test.txt')
    assert problem_two(data) == 12
