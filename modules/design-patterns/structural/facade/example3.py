# https://pythonwife.com/facade-design-pattern-with-python/

class TakeOrder:
   def order(self):
      print("Getting the order.")

class CookPizza:
   def prepare(self):
      print("Preparing the Pizza...")

class Delivery:
   def deliver(self):
      print("Delivered the Pizza.")


class Operator:
	'''Facade Interface'''

	def __init__(self):
		self.ordering = TakeOrder()
		self.preparing = CookPizza()
		self.delivering = Delivery()

	def completeOrder(self):
		self.ordering.order()
		self.preparing.prepare()
		self.delivering.deliver()
		print("Order completed successfully.")


""" main method """
if __name__ == "__main__":
	op = Operator()
	op.completeOrder()