# https://pythonwife.com/flyweight-design-pattern-with-python/

class Arrow:
	def __init__(self, x, y, z, velocity):
		self.x = x
		self.y = y
		self.z = z
		self.velocity = velocity
		self.shape = 'cone'


class ArrowContext:
	def __init__(self, x, y, z, velocity):
		self.x = x
		self.y = y
		self.z = z
		self.velocity = velocity


class ArrowFlyweight:
	def __init__(self):
		self.shape = 'cone'
		self.arrows = []

	def arrow_factory(self, x, y, z, velocity):
		arr = []
		for b in self.arrows:
			if b.x == x and b.y == y and b.z == z and b.velocity == velocity:
				arr.append(b)
		if not arr:
			arr = Arrow(x, y, z, velocity)
			self.arrows.append(arr)
		else:
			arr = arr[0]

		return arr

	def print_arrows(self):
		print('Arrows:')
		for arrow in self.arrows:
			print(str(arrow.x) + ' ' + str(arrow.y) + ' ' + str(arrow.z) + ' ' + str(arrow.velocity))
