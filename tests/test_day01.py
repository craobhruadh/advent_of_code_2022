import pytest
from solutions.day_01 import read_input, problem_one, problem_two


def test_read_input():
    data = read_input('./tests/data/day01_test1.txt')
    assert (len(data) == 5)
    assert (data[0][0] == 1000)
    assert (data[-1][0] == 10000)
    assert (sum(data[0]) == 6000)


def test_problem_one():
    data = read_input('./tests/data/day01_test1.txt')
    assert (problem_one(data) == 24000)


def test_problem_two():
    data = read_input('./tests/data/day01_test1.txt')
    assert (problem_two(data) == 45000)
