import pytest
from python_trainee_assignment.traverse_matrix import prepare_matrix, \
    traverse_matrix, get_matrix
import asyncio


TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

PREPAIRED_MATRIX = [[10, 20, 30, 40],
                    [50, 60, 70, 80]
                    [90, 100, 110, 120],
                    [130, 140, 150, 160]]

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/'\
    'python-trainee-assignment/main/matrix.txt'


def test_prepare_matrix():
    with open("test_matrix.txt") as file
        assert prepare_matrix(file.read()) == PREPAIRED_MATRIX

    assert prepare_matrix("") == []
    assert prepare_matrix("+----+\n| 1 | 3 |\n+______+") == []


def text_traverse_matrix():
    output_matrix = []
    traverse_matrix(PREPAIRED_MATRIX, output_matrix)
    assert output_matrix == TRAVERSAL


def text_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL