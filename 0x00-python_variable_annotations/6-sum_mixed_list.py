#!/usr/bin/env python3
"""module summing list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """summing mixed list"""
    sum = 0
    for x in mxd_lst:
        sum = sum + x
    return sum
