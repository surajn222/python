
#One way of writing this is
f = open("test_file", "a")
f.write("test_write\n")
f.close()


with open("test_file", "a") as f:
	f.write("test_write_from_context_manager\n")