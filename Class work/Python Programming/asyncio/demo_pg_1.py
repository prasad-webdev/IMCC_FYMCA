import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(4)
    print("Welcome to asyncio")

asyncio.run(greet())