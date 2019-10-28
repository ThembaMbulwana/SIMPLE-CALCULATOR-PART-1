from functools import reduce

def add(first_number, second_number,*rest):
    """ Function adds a given set of numbers and returns the total, just like the sum() """
    if len(rest) == 0:
        return first_number + second_number
    else:
        return first_number + second_number + reduce(lambda x, y: x + y, rest)
        
def multiply(first_number, second_number,*rest):
    """ Function multiplies a given set of numbers and returns the total """
    if len(rest) == 0:
        return first_number * second_number
    else:
        return first_number * second_number * reduce(lambda x, y: x * y, rest)