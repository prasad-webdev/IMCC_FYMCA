import asyncio


async def fn():
    print('This is')
    await asyncio.sleep(2)
    print('asynchronous programming')
    await asyncio.sleep(2)
    print('and not multithreading')

asyncio.run(fn())