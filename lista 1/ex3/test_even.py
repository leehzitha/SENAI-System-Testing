from even import isEven

def test_even():
    assert isEven(19) == False
    assert isEven(10) == True
    assert isEven(-2) == True