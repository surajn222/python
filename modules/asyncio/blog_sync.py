import requests
import time

start_time_sync_counter = time.perf_counter()

def function_synchronous_http_request():
    # sending get request and saving the response as response object
    print("Trying to fetch data from httpbin.org")
    response = requests.get(url='https://httpbin.org/get')
    print("\tResponse from website:" + str(response.status_code))
    response.close()
    print("Data fetch complete\n")

def function_main_synchronous():
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

function_main_synchronous()

end_time_sync_counter = time.perf_counter()

print("Total time taken for synchronous code: " + str(end_time_sync_counter-start_time_sync_counter) + "\n\n")