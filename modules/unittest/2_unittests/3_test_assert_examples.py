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

#Assert statements:
# Method	Checks	Version
# assertEqual	a == b
# assertNotEqual	a != b
# assertTrue	bool(x) is True
# assertFalse	bool(x) is False
# assertIs	a is b	2.7
# assertIsNot	a is not b	2.7
# assertIsNone	x is None	2.7
# assertIsNotNone	x is not None	2.7
# assertIn	a in b	2.7
# assertNotIn	a not in b	2.7
# assertIsInstance	is instance(a,b)	2.7
# assertNotIsInstance	not is instance(a,b)	2.7
# assertRaises	fun(*args,**kwds) raises exc
# assertRaisesRegexp	fun(*args,**kwds) raises exc(regex)	2.7
# assertAlmostEqual	round(a-b,7) == 0
# assertNotAlmostEqual	round(a-b,7) != 0
# assertGreater	a > b	2.7
# assertGreaterEqual	a >= b	2.7
# assertLess	a < b	2.7
# assertLessEqual	a <= b	2.7
# assertRegexpMatches	r.search(s)	2.7
# assertNotRegexpMatches	not r.search(s)	2.7
# assertItemsEqual	sorted(a) == sorted(b)	2.7
# assertDictContainsSubset	all the key/value pairs in a exist in b	2.7
# assertMultiLineEqual	strings	2.7
# assertSequenceEqual	sequences	2.7
# assertListEqual	lists	2.7
# assertTupleEqual	tuples	2.7
# assertSetEqual	sets or frozensets	2.7
# assertDictEqual	dicts	2.7