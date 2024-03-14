#!/usr/bin/env python3
"""module for Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function returning a function"""
    def inner(n: float) -> float:
        """function used for mult."""
        return n * multiplier;

    return inner;
