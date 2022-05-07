import unittest

def test_sum(list_integers):
	return sum(list_integers)

def test_sum_tuple(tuple_integers):
	return sum(tuple_integers)

class TestSum(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

	def test_sum_tuple(self):
		self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
	unittest.main()