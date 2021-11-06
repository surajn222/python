import time
import asyncio
import aiohttp

start_time_async_counter = time.perf_counter()

async def coroutine_asynchronous_http_request():
    print("Trying to fetch data from httpbin.org")
    session = aiohttp.ClientSession()
    resp = await session.get(url='https://httpbin.org/get')
    print(resp.status)
    await session.close()
    print("Data fetch complete")

loop = asyncio.get_event_loop()
loop.run_until_complete(
                asyncio.gather(
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request(),
                         coroutine_asynchronous_http_request()
                                )
                        )
# OR
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(coroutine_main_async())

end_time_async_counter = time.perf_counter()

print("Total time taken for asynchronous code: " + str(end_time_async_counter - start_time_async_counter) + "\n\n")
