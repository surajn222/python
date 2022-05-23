#https://medium.com/@yasufumy/python-mock-basics-674c33de1ced

# return value: Completed
# side_effects
# 	timeout
# 	exception
# 	iterator
#
# mock_calls

#Mocking = duplicating a function

#How to "duplicate" a function

#First let's understand what a function is made of.

#Lets take the below example

def execute_query_database():
    print("Connection to a database and query the database")
    return "1,2,3,4"
print("Original function")
print(execute_query_database())
#This function has the below properties
#1. function name
#2. parameter(s)
#3. Execution: may include things like Exception or timeout
#3. return value

#Now lets create a duplicate of this function
import sys
from unittest import mock

mock_execute_query_database = mock.Mock()
mock_execute_query_database.return_value = "1,2,3,4"
print("Mocked function")
print(mock_execute_query_database())
print("We have successfully mocked the function")


#Now lets say this function can have multiple return_values
mock_execute_query_database = mock.Mock()
#mock_execute_query_database.return_value = "1,2,3,4"
mock_execute_query_database.side_effect = ["4,3,2,1", "1,2,3,4"]
print("Mocked function side effect")
print(mock_execute_query_database())
print("We have successfully mocked the function")

#Now lets add some properties to the function, like multiple return values

def execute_query_database(sql_query):
    print("Connection to a database and query the database")
    if sql_query == "sql_query_1":
        return "1,2,3,4"
    else:
        return "4,3,2,1"

print("Original function 2")
print(execute_query_database("sql_query_1"))

#Now the return value depends on the input. How to mock this function? Here we go:
def mock_execute_query_database_side_effect(sql_query):
    print("Connecting to database, running sql query and fetching data")
    if sql_query == "sql_1":
        return "1,2,3,4"
    elif sql_query == "sql_2":
        return "4,3,2,1"


mock_execute_query_database = mock.Mock()
mock_execute_query_database.side_effect = mock_execute_query_database_side_effect
print("Mocked function 2")
print(mock_execute_query_database("sql_1"))
print(mock_execute_query_database("sql_2"))


print("Function 3")
def execute_query_database(sql_query):
    print("Connection to a database and query the database")
    if isinstance(sql_query, int):
        raise ValueError("Incorrect sql query")
    if sql_query == "sql_query_1":
        return "1,2,3,4"
    else:
        return "4,3,2,1"

def mock_execute_query_database_side_effect(sql_query):
    print("Connecting to database, running sql query and fetching data")
    if isinstance(sql_query, int):
        raise ValueError("Incorrect sql query")
    if sql_query == "sql_1":
        return "1,2,3,4"
    elif sql_query == "sql_2":
        return "4,3,2,1"

mock_execute_query_database.side_effect = mock_execute_query_database_side_effect

mock_execute_query_database = mock.Mock()
mock_execute_query_database.side_effect = mock_execute_query_database_side_effect
print("Mocked function 3")
print(mock_execute_query_database("sql_1"))
print(mock_execute_query_database("sql_2"))
print(mock_execute_query_database(1))

print("Here")

sys.exit()

#Mock is an object of class mock.Mock()
#Mock object has to be first created, then its return value has to be assigned
#For eg.
#mock_obj = mock.Mock()
#mock_obj.return_value = 42
#Then when you print mock_obj, it will give you a value of 42

#Lets say the get function in the requests lib is what you want to mock
#You create a mock object and assign it to requests lib
#requests = mock.Mock()
#requests.get.return_value = {"json_key": "json_value", "status_code": "200"}
#requests.get.return_value.status_code = 200


#Example 0

#Lets say you have this function
import sys
from unittest import mock


requests = mock.Mock()
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
print(requests.mock_calls)
print(requests.mock_calls[0])

print(requests.mock_calls[0][0])
print(requests.mock_calls[0][1])
print(requests.mock_calls[0][2])

m = mock.Mock(side_effect=lambda x: x % 2 == 0)
print(m(42))
print(m(11))

m = mock.Mock(return_value=lambda x: x % 2 == 0)
print(m(42))
print(m(11))


sys.exit()
call_info = requests.mock_calls[0]
print(call_info[0])
print(call_info[1])
print(call_info[2])


sys.exit()


def get_data_from_database():
    print("Connecting to database, running sql query and fetching data")
    return "1,2,3,4"

print(get_data_from_database())

print("Now you want to mock this function")
print("You create a mock object with the same properties as the actual object and assign it to the mock object")
mock_obj = mock.Mock()
mock_obj.return_value = "1,2,3,4"
print(mock_obj)

get_data_from_database = mock_obj
print(get_data_from_database())




def get_data_from_database_parameters(sql_query):
    print("Connecting to database, running sql query and fetching data")
    if sql_query == "sql_1":
        return "1,2,3,4"
    elif sql_query == "sql_2":
        return "4,3,2,1"

print(get_data_from_database_parameters("sql_1"))

print("Now you want to mock this function")
print("You create a mock object with the same properties as the actual object and assign it to the mock object")

def mock_get_data_from_database(sql_query):
    mock_obj = mock.Mock()
    print("Connecting to database, running sql query and fetching data")
    if sql_query == "sql_1":
        mock_obj.return_value = "1,2,3,4"
    elif sql_query == "sql_2":
        mock_obj.return_value = "4,3,2,1"
    return mock_obj

get_data_from_database_parameters.side_effect = mock_get_data_from_database
print("Here")
print(get_data_from_database_parameters("sql_1"))
print(get_data_from_database_parameters("sql_2"))



sys.exit()

#Example 1
import sys

from unittest import mock



mock_obj = mock.Mock()
mock_obj.get.return_value.status_code = 200

requests= mock_obj

r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
print(r.status_code)

#Example 2
from unittest import mock

requests = mock.Mock()
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))

m = mock.Mock()
m.can.access.any.attribute = 1

m = mock.Mock()
m.can.accept.any.call('with', 'any', 'argument', [1, 2, 3])

#Example 3
#method1
m = mock.Mock(return_value=42)
print(m())

#method2
print("here")
m = mock.Mock()
m.return_value = 42
print(m())

#method3
m = mock.Mock(return_value=42)
print(m.any.method())

sys.exit()

requests = mock.Mock()
requests.get.return_value.status_code = 200
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
print(r.status_code)

r = requests.get('invalid_url')
print(r.status_code)


def return_status_code(url, *args, **kwargs):
    m = mock.Mock()
    code = 200 if url == 'https://api.github.com/user' else 404
    m.status_code = code
    return m

requests = mock.Mock()
requests.get.side_effect = return_status_code
print(requests.get('https://api.github.com/user',auth=('user', 'pass')).status_code)
print(requests.get('invalid_url').status_code)


requests = mock.Mock()
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
requests.mock_calls
print(requests.mock_calls[0])

call_info = requests.mock_calls[0]
print(call_info[0])
print(call_info[1])
print(call_info[2])


m = mock.Mock(side_effect=lambda x: x % 2 == 0)
print(m(42))
print(m(11))

sys.exit()

requests = mock.Mock()
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
requests.get.assert_called_once_with(
        'https://api.github.com/user', auth=('user', 'pass'))

sys.exit()


from unittest import mock
import mock

m = mock.Mock()
dir(m)

m.some_attribute.return_value = 42

m.some_attribute()

def print_answer():
    print("42")

m.some_attribute.return_value = print_answer
m.some_attribute()

m.some_attribute.side_effect = ValueError('A custom value error')
m.some_attribute()


m.some_attribute.side_effect = range(3)
m.some_attribute()
0
m.some_attribute()
1
m.some_attribute()
2
m.some_attribute()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.4/unittest/mock.py", line 902, in __call__
#     return _mock_self._mock_call(*args, **kwargs)
#   File "/usr/lib/python3.4/unittest/mock.py", line 961, in _mock_call
#     result = next(effect)
# StopIteration



def print_answer():
    print("42")
m.some_attribute.side_effect = print_answer
m.some_attribute()


def print_number(num):
    print("Number:", num)

m.some_attribute.side_effect = print_number
m.some_attribute.side_effect(5)

sys.exit()




#MagicMock
m = mock.Mock()
#m['any_key_you_want']
#This won't work

m = mock.Mock()
for x in m:
    print(m)
#This won't work either


requests = mock.MagicMock()
print(requests.unwanted_method())



import requests
mock_requests = mock.MagicMock(spec=requests)
print(mock_requests.unwanted_method())
#This will fail


import requests
mock_requests = mock.MagicMock(spec=requests)
r = mock_requests.Session()
r.unwanted_method()



import requests
mock_requests = mock.create_autospec(spec=requests)
r = mock_requests.Session()
r.unwanted_method()