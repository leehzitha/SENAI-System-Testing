from menor import menor

def test_menor():
    assert menor(9, 2, 1) == 1
    assert menor(2, 1, 9) == 1
    assert menor(9, 1, -10) == -10