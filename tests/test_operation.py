from src.math_opearation import add, subtract   


def test_add():

    assert add(2,3)==5
    assert add(-1,1)==0

    assert subtract(5,3)==2

def test_sub():
    assert subtract(5,3)==2
    assert subtract(4,3)==1
    assert subtract(3,3)==0
    assert subtract(2,3)==-1