import asyncio 

async def square(n):
    await asyncio.sleep(2)
    return n * n

async def main():
    result = await asyncio.gather(
        square(1),          
        square(2),
        square(3),
    )

    print(result)

asyncio.run(main())