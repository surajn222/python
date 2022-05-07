import unittest

class Sum_class:
	def test_sum(self, list_integers):
		return sum(list_integers)

	def test_sum_tuple(self, tuple_integers):
		return sum(tuple_integers)

class TestSum(unittest.TestCase):
	def test_sum(self):
		sum = Sum_class()
		self.assertEqual(sum.test_sum([1, 2, 3]), 6, "Should be 6")

	def test_sum_tuple(self):
		sum = Sum_class()
		self.assertEqual(sum.test_sum_tuple((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
	unittest.main()