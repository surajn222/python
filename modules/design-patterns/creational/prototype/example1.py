# https://stackabuse.com/the-prototype-design-pattern-in-python/
from abc import ABC, abstractmethod
import copy
import time

# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(3)
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass

class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(3)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30

    # Overwritting Cloning Method:
    def clone(self):
        return copy.deepcopy(self)

class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        # Concrete class attribute
        self.stamina = 60
    # Overwritting Cloning Method
    def clone(self):
        return copy.deepcopy(self)

class Mage(Prototype):
     def __init__(self, height, age, defense, attack):
     # Call superclass constructor, time.sleep() and assign base values
     self.mana = 100

    # Overwritting Cloning Method
    def clone(self):
        return copy.deepcopy(self)

print('Starting to create a Shopkeeper NPC: ', datetime.datetime.now().time())
shopkeeper = Shopkeeper(180, 22, 5, 8)
print('Finished creating a Shopkeeper NPC: ', datetime.datetime.now().time())
print('Attributes: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))