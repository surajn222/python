#f = open("test_file", "w") #This part will be context managerised
#f.write("Test")
#f.close() #This part will be context managerised

class Open_File():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.file.close()

with Open_File("test_file", "w") as f:
	f.write("from context manager class\n")