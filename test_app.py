from app import find_pairs_with_sum

def test_find_pairs_with_sum():
    numbers, target = [ 1, 9, 5, 0, 20, -4, 12, 16, 7] , 12
    assert find_pairs_with_sum(numbers, target) == [(0, 12), (-4, 16), (5, 7)]
