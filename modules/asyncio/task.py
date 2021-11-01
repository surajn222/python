import asyncio
async def async_func():
    print('Velotio ...')
    await asyncio.sleep(10)
    print('... Blog!')

async def main():
    task1 = asyncio.create_task (async_func())
    task2 = asyncio.create_task(async_func())
    await task1
    await task2
asyncio.run(main())