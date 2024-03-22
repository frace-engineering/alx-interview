#!/usr/bin/python3
"""Calculate minimum operations to achieve a result."""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given
    a number n, write a method that calculates the fewest number of
    operations needed to result in exactly nH characters in the file.

    Args:
        n of type integer.

    Return:
        Minimum number of operations
    """
    if n == 1:
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
