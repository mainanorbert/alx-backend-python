#!/usr/bin/env python3
"""module for string and int/float to tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of str and int/float"""
    return (k, float(v * v))
