#!/usr/bin/env python3
"""A module with rite an asynchronous coroutine"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """a function that waits for a random delay
    between 0 and max_delay (included and float value)
    seconds and eventually returns "the delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
