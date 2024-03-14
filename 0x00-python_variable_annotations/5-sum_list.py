#!/usr/bin/env python3
"""module  that sums a list"""


def sum_list(input_list: list[float]) -> float:
    """function returning sum of numbers in a list"""
    sum: float = 0
    for x in input_list:
        sum = sum + x
    return (sum)
