#!/usr/bin/env python3
"""module for Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function taking float argument and returns a
    function that multiplies two floats
    """
    def inner(n: float) -> float:
        """function used for mult."""
        return n * multiplier

    return inner
