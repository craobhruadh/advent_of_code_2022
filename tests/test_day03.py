import pytest
from solutions.day_03 import read_file, problem_one, problem_two, get_priority_dictionary


def test_read_file():
    data = read_file('./tests/data/day03_test.txt')
    assert data[0][0] == 'vJrwpWtwJgWr'
    assert data[0][1] == 'hcsFMMfFFhFp'
    assert data[1][0] == 'jqHRNqRjqzjGDLGL'
    assert data[1][1] == 'rsFMfFZSrLrFZsSL'


def test_get_priority_dictionary():
    dict_priorites = get_priority_dictionary()
    assert dict_priorites['a'] == 1
    assert dict_priorites['z'] == 26
    assert dict_priorites['A'] == 27
    assert dict_priorites['Z'] == 52


def test_problem_one():
    data = read_file('./tests/data/day03_test.txt')
    assert problem_one(data) == 157


def test_problem_two():
    data = read_file('./tests/data/day03_test.txt')
    assert problem_two(data) == 70
