#!/usr/bin/python3
"""Minimum Operations"""


import math


def minOperations(n):
      """
    Calculate the minimum number of operations to reach n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations