#!/usr/bin/env python3
"""a module  that takes an integer
max_delay and returns a asyncio.Task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """function returning asyncio.Task"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
