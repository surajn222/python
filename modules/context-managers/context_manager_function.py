from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
	f = open(file, mode)
	yield f
	f.close()


with open_file("test_file", "w") as f:
	f.write("from contxt manager function")

print(f.closed)