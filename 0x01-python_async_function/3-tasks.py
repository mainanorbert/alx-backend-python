#!/usr/bin/env python3
"""
a module  that turns a asyncio.Task
"""

from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """function returning asyncio.Task"""
    task = create_task(wait_random(max_delay))
    return task
