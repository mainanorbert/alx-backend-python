#!/usr/bin/env python3
"""module that returns list of delays"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function returns list of delays"""
    delay = await asyncio.gather(*[task_wait_random(max_delay)
                                   for _ in range(n)])
    return sorted(delay)