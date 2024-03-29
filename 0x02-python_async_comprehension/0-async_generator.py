#!/usr/bin/env python3
"""module the define async func"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a coroutine generating int btn (1, 10)"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
