def palindrome(palabra):
    """
     Check if a word is a palindrome. The palindromes are
     words or phrases that are read equally from both sides.
     If it is a palindrome it returns True and if not False

    >>> palindrome("radar")
    True

    >>> palindrome("somos")
    True

    >>> palindrome("holah")
    False

    >>> palindrome("Ana")
    True

    >>> palindrome("Atar a la rata")
    True

    """

    # Check is if the same as in opossite
    if palabra.lower().replace(" ", "") == palabra[::-1].lower().replace(" ", ""): 
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()