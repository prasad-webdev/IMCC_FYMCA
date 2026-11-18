import asyncio 

async def example():
    print("Task started")
    await asyncio.sleep(3)
    print("Task completed")

asyncio.run(example())
