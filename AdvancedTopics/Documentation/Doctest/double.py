def double_value(lis):
    """
    Double the value of the items in a list
    >>> l = [1, 2, 3, 4, 5] 
    >>> double_value(l)
    [2, 4, 6, 8, 10]

    >>> l = []
    >>> for i in range(10):
    ...     l.append(i)
    >>> double_value(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

    """
    return [n*2 for n in lis]

if __name__ == "__main__":
    import doctest
    doctest.testmod()