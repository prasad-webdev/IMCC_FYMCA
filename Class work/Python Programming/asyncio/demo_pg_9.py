import asyncio

async def main():
    task = asyncio.create_task(fn2())
    print("One")
    print("Four")
    await asyncio.sleep(3)
    print("Five")
    await asyncio.sleep(1)

async def fn2():
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(4)
    print("Three")

asyncio.run(main())