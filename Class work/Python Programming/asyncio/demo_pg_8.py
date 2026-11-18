import asyncio

async def main():

    print("One")
    await asyncio.sleep(1)
    await fn2()

    print("Four")
    await asyncio.sleep(1)

    print("Five")
    await asyncio.sleep(1)

async def fn2():
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)
    print("Three")

asyncio.run(main())