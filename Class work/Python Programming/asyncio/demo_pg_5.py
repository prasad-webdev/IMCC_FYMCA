import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(3)
    print(f"{name} completed")

async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )

asyncio.run(main())