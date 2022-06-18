from abc import abstractmethod


class Component():

	@abstractmethod
	def operation(self):
		pass


class Composite(Component):
	""" Composite Interface """

	def __init__(self):
		self._children = set()

	def operation(self):
		for child in self._children:
			child.operation()

	# Method to add Leaves
	def add(self, component):
		self._children.add(component)

	# Method to remove Leaves
	def remove(self, component):
		self._children.discard(component)


class Leaf(Component):
	""" Leaf """

	def operation(self):
		pass


# Driver Code
def main():
	leaf = Leaf()
	composite = Composite()
	composite.add(leaf)
	composite.operation()


if __name__ == "__main__":
	main()