import unittest

def broken_function():
    raise Exception('This is broken')


def broken_function_2():
    raise ValueError('Value Error Exception')

def broken_function_3():
    raise TypeError('Type Error Exception')

class MyTestCase(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(Exception) as context:
           broken_function()

    def test_value_error(self):
        with self.assertRaises(ValueError) as context:
            broken_function_2()

    def test_type_error(self):
        with self.assertRaises(TypeError) as context:
            broken_function_3()

        #self.assertTrue('This is broken' in context.exception)

if __name__ == '__main__':
    unittest.main()