# Working
# https://pythonwife.com/bridge-design-pattern-with-python/
from abc import abstractmethod

"""Abstract class for Shapes"""


class shape:
	def no_of_sides(self, sides):
		self.sides = sides

	def set_color(self, color):
		self.color = color._color

	@abstractmethod
	def Find_area(self):
		pass


class Square(shape):
	def __init__(self, width, sides, color):
		self.width = width
		super().no_of_sides(sides)
		super().set_color(color)

	def Find_area(self):
		return self.width ** 2

	"""Method to get information of the class."""

	def __str__(self):
		return f'Shape: {type(self).__name__}, Side: {self.sides}, Colour: {self.color}, Area: {self.Find_area()}'


class Circle(shape):
	def __init__(self, radius, sides, color):
		self.radius = radius
		super().no_of_sides(0)
		super().set_color(color)

	def Find_area(self):
		return 3.14 * self.radius ** 2

	def __str__(self):
		return f'Shape: {type(self).__name__}, Side: {self.sides}, Colour: {self.color}, Area: {self.Find_area()}'


"""Interface for implementation"""


class Color:
	def fill_color(self):
		pass


"""Subclass for implementation interface."""


class RedColor(Color):
	def __init__(self):
		self.fill_color()

	def fill_color(self):
		self._color = 'Red'


class BlueColor(Color):
	def __init__(self):
		self.fill_color()

	def fill_color(self):
		self._color = 'Blue'


# Driver Code
objS = Square(4, 4, RedColor())
objC = Circle(2, 0, BlueColor())
print(objS, objC, sep="\n")