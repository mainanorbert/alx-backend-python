#!/usr/bin/env python3
"""module  that sums a list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function returning sum of numbers in a list"""
    sum: float = 0
    for x in input_list:
        sum = sum + x
    return (sum)
