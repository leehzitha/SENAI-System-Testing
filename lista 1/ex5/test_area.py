import math

from area import square, triangle, elipse

def test_square():
    assert square(5, 10) == 50
    assert square(5, 10) == square(10, 5)

def test_triangle():
    assert triangle(5, 10) == 25

def test_elipse():
    assert elipse(5, 3) == math.pi * 15
    assert elipse(5, 3) == elipse(3, 5)