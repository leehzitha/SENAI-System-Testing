from conversao import *
import pytest

def test_measures():
    assert toMetro(100) == 1
    assert toCm(1) == 100

def test_volume():
    assert toLitro(1000) == 1
    assert toMl(1) == 1000

def test_money():
    assert toDolar(15) == 3.04
    assert toReal(15) == 73.95 