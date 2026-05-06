from calc import soma, sub, div, mult

def test_soma():
    assert soma(1, -5) == -4

def test_sub():
    assert sub(-1, -10) == 9

def test_mult():
    assert mult(8, 9) == 72

def test_div():
    assert div(10, 5) == 2
    assert div(10, 0) == 'error'