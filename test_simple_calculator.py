from simple_calculator import *



def test_add():
	assert add(0,0) == 0
 
def test_add_negative():
    assert add(-1,-1) == -2

def test_add_random():
    assert add(4,5) == 9
    
def test_add_more_numbers():
    assert add(1,2,3,4) == 10
    
def test_multiply():
    assert multiply(1,2) == 2
 
def test_multiply_many():
    assert multiply(1,2,3,4) == 24
