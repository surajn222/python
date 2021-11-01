import asyncio


async def async_func():
    print('Velotio ...')
    await asyncio.sleep(5)
    print('... Technologies!')

async def main():
    async_func()
    await async_func()

asyncio.run(main()) #This is the event loop