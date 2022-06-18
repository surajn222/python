# Working
# https://www.youtube.com/watch?v=_jBjhI6-VDI&t=503s

from abc import ABCMeta, abstractstaticmethod
import copy

class IProtoType(metaclass=ABCMeta):
	@abstractstaticmethod
	def clone():
		pass

class ConcreteClass1(IProtoType):

	def __init__(self, i=0, s="", l=[], d={}):
		self.i = i
		self.s = s
		self.l = l
		self.d = d

	def clone(self):
		return type(self)(self.i, self.s, self.l.copy(), self.d.copy())

	def __str__(self):
		return f"{self.i}\t{self.s}\t{self.l}\t{self.d}"

class ConcreteClass2(IProtoType):

	def __init__(self, i=0, s="", l=[], d={}):
		self.i = i
		self.s = s
		self.l = l
		self.d = d

	def clone(self):
		return type(self)(self.i, self.s, copy.deepcopy(self.l), copy.deepcopy(self.d))

	def __str__(self):
		return f"{self.i}\t{self.s}\t{self.l}\t{self.d}"



if __name__ == "__main__":
	object1 = ConcreteClass1(1, "class1", [1,2], {"a": "1"})
	print(object1)



