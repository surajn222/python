import asyncio
import aiohttp
import async_timeout


async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def main(loop):
    print(1)
    async with aiohttp.ClientSession(loop=loop) as session:
        future = asyncio.ensure_future(fetch(session, 'http://python.org')) # we start the fetch process
        print(2)
        html = await future # we wait for getting the fetch response
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))