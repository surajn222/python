# Working
# https://pythonwife.com/prototype-design-pattern-with-python/
class Car:
        def __init__(self, engine="1500cc", color="D-white", seats=7):
                self.engine = engine
                self.color = color
                self.seats = seats
        def __str__(self):
                return  f'{self.engine} | {self.color} | {self.seats}'


import copy
class Prototype:
        def __init__(self):
                '''Dictionary that will stores cloned objects.'''
                pass

        def Clone(self, object, **kwargs):
                """Method to clone the object."""
                clonedObject = copy.deepcopy(object)
                clonedObject.__dict__.update(kwargs)
                return clonedObject


if __name__ == "__main__":
    """The object that will be cloned.""" 
    defaultCar = Car()
    prototype = Prototype()

    """The object that will be cloned.""" 
    CarType1 = Car("1000cc", "Red", 4)

    # """Registering the defaultCar in dictionary with its key as 'basicCar'"""
    # prototype.RegisterObject('BasicCar', defaultCar)
    # prototype.RegisterObject('Type-1', CarType1)

    CloneCarOne = prototype.Clone(CarType1, color = "Lake side brown")
    # carTwo = prototype.Clone('Type-1',color = "Red")
    # carThree = prototype.Clone('Type-1', color = "Moon Dust Silver")

    print("Details of the default-car:", defaultCar)
    print("Details of CarType1:", CarType1)
    print("Details of CloneCarOne:", CloneCarOne)
    # print("Details of car-Two:", carTwo)
    # print("Details of car-Three:", carThree)