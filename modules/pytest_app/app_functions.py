import os
import sys

def execute_query_database_1():
    execute_query_database_2("sql_1")
    return "1,2,3,4"

def execute_query_database_2(sql_query):
    print("Connection to a database and query the database")
    if sql_query == "sql_query_1":
        return "1,2,3,4"
    else:
        return "4,3,2,1"

def execute_query_database_3(sql_query):
    print("Connection to a database and query the database")
    if isinstance(sql_query, int):
        raise ValueError("Incorrect sql query")
    if sql_query == "sql_query_1":
        return "1,2,3,4"
    else:
        return "4,3,2,1"

def work_on():
    path = os.getcwd()
    print(f'Working on {path}')
    return path

#execute_query_database_1()
