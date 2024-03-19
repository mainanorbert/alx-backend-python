#!/usr/bin/env python3
import asyncio

async def async_generator():
    for i in range(5):
        yield i
        await asyncio.sleep(0.1)

async def main():
    result = [x async for x in async_generator()]
    print(result)

asyncio.run(main())

