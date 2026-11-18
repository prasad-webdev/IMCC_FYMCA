import asyncio

async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 completed")

async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 completed")

async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 completed")

async def main():
    L = await asyncio.gather(
        func1(),    
        func2(),
        func3()
    )

    print("Main Ended..")

asyncio.run(main())