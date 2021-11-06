import asyncio

async def hello(i):
    print(f"hello {i} started")
    await asyncio.sleep(4)
    print(f"hello {i} done")

async def main():
    task1 = asyncio.create_task(hello(1))  # returns immediately, the task is created
    await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

asyncio.run(main())  # main loop