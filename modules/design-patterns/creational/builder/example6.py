# https://pythonwife.com/builder-design-pattern/


class Car():
	'''The Product'''

	def __init__(self):
		self.autonomous_driving = False
		self.sunroof = False
		self.fuel = None

	# Methods to add features
	def addAutonomous_driving(self):
		self.autonomous_driving = True

	def addSunroof(self):
		self.sunroof = True

	def addFuel(self, fuel="Electric"):
		self.fuel = fuel

	# Returning information about car
	def __str__(self):
		return f'Autonomous driving: {self.autonomous_driving} | Sunroof: {self.sunroof} | Fuel: {self.fuel}'

ModelOne = Car()
# First instance name ModelOneModelOne = Car()
ModelOne.addAutonomous_driving()
ModelOne.addSunroof()
ModelOne.addFuel("Petrol")
print("Details of car:", ModelOne)

# Second instance named ModelTwo
ModelTwo = Car()
ModelTwo.addAutonomous_driving()
ModelTwo.addFuel()
print("Details of car:", ModelTwo)

# Third instance named ModelThree
ModelThree = Car()
ModelThree.addAutonomous_driving()
ModelThree.addSunroof()
ModelThree.addFuel("Diesel")
print("Details of car:", ModelThree)