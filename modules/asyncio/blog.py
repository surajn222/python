import os
import sys
import aiohttp
import asyncio
import requests
import time

start_time_sync_counter = time.perf_counter()

def function_synchronous_http_request():
    # sending get request and saving the response as response object
    print("Trying to fetch data from httpbin.org")
    response = requests.get(url='https://httpbin.org/get')
    print("\tResponse from website:" + str(r.status_code))
    response.close()
    print("Data fetch complete\n")

def function_main_sync():
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()
    function_synchronous_http_request()

function_main_sync()

end_time_sync_counter = time.perf_counter()

print("Total time taken for synchronous code: " + str(end_time_sync_counter-start_time_sync_counter) + "\n\n")
#===================================================================================================

start_time_async_counter = time.perf_counter()

async def coroutine_asynchronous_http_request():
    print("Trying to fetch data from httpbin.org")
    session = aiohttp.ClientSession()
    resp = await session.get(url = 'https://httpbin.org/get')
    print(resp.status)
    await session.close()
    print("Data fetch complete")

async def coroutine_main_async():
    await asyncio.gather(coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request(),coroutine_asynchronous_http_request())


# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(coroutine_main_async())
#OR
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine_main_async())

end_time_async_counter = time.perf_counter()


print("Total time taken for asynchronous code: " + str(end_time_async_counter-start_time_async_counter) + "\n\n")

# first_awaitable = asyncio.create_task(print_after("world!", 2))
# second_awaitable = asyncio.create_task(print_after("Hello", 1))

#asyncio function
#process = await asyncio.create_subprocess_exec("echo", string)




