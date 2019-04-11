def sumTwo(a, b):
    """
    This function receives two parameters a & b:
    Returns the sum of both
    
    Can test sum of numbers: 

    >>> sumTwo(5,10)
    15

    >>> sumTwo(1,0)
    1
    
    >>> sumTwo(-5,7)
    2

    Strings of text:

    >>> sumTwo('aa','bb')
    'aabb'

    Or lists:

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> sumTwo(a,b)
    [1, 2, 3, 4, 5, 6]

    Sum different types of data:

    >>> sumTwo(10,'hello')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'


    """
    return a+b


if __name__ == "__main__":
    import doctest
    doctest.testmod()