#!/usr/bin/env python3
"""module to Duck typing - first element of a sequence"""

from typing import Optional, Any


def safe_first_element(lst: List[Any]) -> Any:
    """Returns the first element of a list, or None if the list is empty."""
    if lst:
        return lst[0]
    else:
        return None
