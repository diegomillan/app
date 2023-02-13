import pytest
from app import find_pairs_with_sum

@pytest.fixture
def input():
    return [ 1, 9, 5, 0, 20, -4, 12, 16, 7] , 12

def test_find_pairs_with_sum(input):
    numbers, target = input
    assert find_pairs_with_sum(numbers, target) == [(0, 12), (-4, 16), (5, 7)]
