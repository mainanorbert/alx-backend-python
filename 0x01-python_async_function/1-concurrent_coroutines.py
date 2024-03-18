#!/usr/bin/env python3
"""Module that execute multiple
coroutines at the same time with async"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''function that returns a list of delays'''
    d_list = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(d_list)
