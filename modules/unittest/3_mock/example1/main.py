#https://www.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
from unittest import mock

#Creating an object and checking functions of it
m = mock.Mock()
print(dir(m))

m.some_attribute
print(dir(m))
print(m.some_attribute)

m.some_attribute.return_value = 42
print(m.some_attribute.return_value)

def print_answer():
	print("42")

m.some_attribute.return_value = print_answer
m.some_attribute.return_value()

m.some_attribute.side_effect = range(3)
print(m.some_attribute())
print(m.some_attribute())
print(m.some_attribute())

#m.some_attribute_2.side_effect = ValueError('A custom value error')
#m.some_attribute_2()


def print_answer(num):
	print(num)

m.some_attribute_3.side_effect = print_answer
m.some_attribute_3(52)



class Number(object):
	def __init__(self, value):
		self._value = value
	def print_value(self):
		print("Value:", self._value)

m.some_attribute.side_effect = Number
n = m.some_attribute.side_effect(26)
n
n.print_value()