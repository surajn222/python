import time

class Calculator:
    def sum(self, a, b):
        time.sleep(10) # long running process
        return a + b

    def mul(self, a, b):
        time.sleep(10)  # long running process
        return a * b


from unittest import TestCase
from unittest.mock import patch

class TestCalculator(TestCase):
    @patch('1_patch_example.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)