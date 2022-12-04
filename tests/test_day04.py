import pytest
from solutions.day_04 import read_file, problem_one, problem_two


def test_read_file():
    data = read_file('./tests/data/day04_test.txt')
    assert len(data) == 6
    assert data[0][0] == [2, 4]
    assert data[0][1] == [6, 8]
    assert data[-1][0] == [2, 6]
    assert data[-1][1] == [4, 8]


def test_problem_one():
    data = read_file('./tests/data/day04_test.txt')
    assert (problem_one(data) == 2)


def test_problem_two():
    data = read_file('./tests/data/day04_test.txt')
    assert problem_two(data) == 4
