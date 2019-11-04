from simple_calculator import *



def test_add():
	assert simple_calculator.add(0,0) == 0
 
def test_add_negative():
    assert simple_calculator.add(-1,-1) == -2

def test_add_random():
    assert simple_calculator.add(4,5) == 9
    
def test_add_more_numbers():
    assert simple_calculator.add(1,2,3,4) == 10
    
def test_multiply():
    assert simple_calculator.multiply(1,2) == 2
 
def test_multiply_many():
    assert simple_calculator.multiply(1,2,3,4) == 24
