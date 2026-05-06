from salLiq import calcSal

def test_menor_5000():
    assert calcSal(100, 40) == 3560

def test_maior_5000():
    assert calcSal(100, 51) == 4131

def test_igual_5000():
    assert calcSal(100, 50) == 4450
