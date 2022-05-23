#Mocking = duplicating a function

#How to "duplicate" a function

#First let's understand what a function is made of.

#Take the below example
def execute_query_database(sql_query):
    print("Connection to a database and query the database")
    if isinstance(sql_query, int):
        raise ValueError("Incorrect sql query")
    if sql_query == "sql_query_1":
        return "1,2,3,4"
    else:
        return "4,3,2,1"

print("Original function")
print(execute_query_database("sql_query_1"))

#Every function function has the below properties
#1. function name
#2. parameter(s) (Optional)
#3. Execution/Body: may include things like Exception or timeout (In Mocking, this is called side effects. Will come back to this later)
	#a. Exception
	#b. Timeout
    #c. Iterator
#4. return value (In Mocking, this is called return_value. Will come back to this later)

#In short, we have to mock all of the return values (Everything inside Execution body, that includes return_value)

#Lets start mocking one thing at a time

# return value: Example 1
# side_effects
#   multiple return values based on input parameters Example 2
# 	timeout
# 	exception Example 3
# 	iterator
#
# mock_calls Example 4

#Example 1: -------------------------------------------------------------
def execute_query_database():
    return "1,2,3,4"

#Now lets create a duplicate/mock of this function
from unittest import mock

mock_execute_query_database = mock.Mock() #Create Mock Object
mock_execute_query_database.return_value = "1,2,3,4" #Assign return value
print("Mocked function")
print(mock_execute_query_database()) #Call the mock function
print("We have successfully mocked the function")
#Example 1 end: -------------------------------------------------------------



#Example 2: -------------------------------------------------------------
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

#Side effect can also be written this way:
#Now lets say this function can have multiple return_values
mock_execute_query_database = mock.Mock()
mock_execute_query_database.side_effect = ["4,3,2,1", "1,2,3,4"]
print("Mocked function side effect")
print(mock_execute_query_database())
print("We have successfully mocked the function")

#Example 2 end: -------------------------------------------------------------

#Example 3: -------------------------------------------------------------
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
#print(mock_execute_query_database(1))

#Example 3 end: -------------------------------------------------------------

#Example 4: -------------------------------------------------------------
print("Mock calls")
print(mock_execute_query_database.mock_calls)

# print(requests.mock_calls[0][0])
# print(requests.mock_calls[0][1])
# print(requests.mock_calls[0][2])



#Finally, lets check all available functions in the mock object
print(dir(mock))