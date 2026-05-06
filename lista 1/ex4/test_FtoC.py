from FtoC import Cel_to_Fahr, Fahr_to_Cel

def test_Cel():
    assert Cel_to_Fahr(90) == 194
    assert Fahr_to_Cel(50) == 10