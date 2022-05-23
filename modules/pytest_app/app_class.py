import os
import sys

class database:
	def __init__(self, creds):
		self.creds = creds

	def execute_query_database_1(self):
		self.execute_query_database_2("sql_1")
		return "1,2,3,4"

	def execute_query_database_2(self, sql_query):
		print("Connection to a database and query the database")
		if sql_query == "sql_query_1":
			return "1,2,3,4"
		else:
			return "4,3,2,1"

	def execute_query_database_3(self, sql_query):
		print("Connection to a database and query the database")
		if isinstance(sql_query, int):
			raise ValueError("Incorrect sql query")
		if sql_query == "sql_query_1":
			return "1,2,3,4"
		else:
			return "4,3,2,1"
