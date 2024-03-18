#!/usr/bin/env python3
""" module that measures the runtime"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function measuring execution time for wait_n"""
    s_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    e_time = time.time()
    t_time = e_time - s_time
    return t_time / n
