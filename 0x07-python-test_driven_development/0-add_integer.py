#!/usr/bin/python3
#!/usr/bin/python3
'''A function that adds 2 integers'''


def add_integer(a, b=98):
    '''Returns the sum of a and b
    and also the result int datatype.
    Raises TypeError if data is diferrent that int.
    '''
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
