#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates the length of each element in a list of strings."""
    return [(i, len(i)) for i in lst]
