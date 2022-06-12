# https://machinelearningmastery.com/a-gentle-introduction-to-decorators-in-python/

def repeat(fn):
	fn()
	fn()


def hello_world():
	print("Hello world!")


repeat(hello_world)


def repeat_decorator(fn):
	def decorated_fn():
		fn()
		fn()

	# returns a function
	return decorated_fn


def hello_world():
	print("Hello world!")


hello_world_twice = repeat_decorator(hello_world)

# call the function
hello_world_twice()