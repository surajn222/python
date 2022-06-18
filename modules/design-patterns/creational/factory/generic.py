#               AbstractClass
#                   abstract_method_1
#                   abstract_method_2
# ConcreteClass1                ConcreteClass2
#   abstract_method_1               abstract_method_1
#   abstract_method_2               abstract_method_2
#
# Factory
#   create_object(class_name)
#       returns -> ConcreteClass1 | ConcreteClass2 | ConcreteClass3
#
# client -> factory.create_object
import abc

class AbstractClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abstract_method_1(self):
        pass

    @abc.abstractmethod
    def abstract_method_2(self):
        pass

class ConcreteClass1(AbstractClass):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def abstract_method_1(self):
        return self.param1 * self.param2

    def abstract_method_2(self):
        return 2 * (self.param1 + self.param2)

class ConcreteClass2(AbstractClass):
    def __init__(self, param1):
        self.param1 = param1

    def abstract_method_1(self):
        return self.param1 ** 2

    def abstract_method_2(self):
        return 4 * self.param1

class ConcreteClass3(AbstractClass):
    def __init__(self, param1):
        self.param1 = param1

    def abstract_method_1(self):
        return 3.14 * self.param1 * self.param1

    def abstract_method_2(self):
        return 2 * 3.14 * self.param1

class Factory:
    def create_object(self, name):
        if name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return ConcreteClass2(float(radius))

        elif name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return ConcreteClass1(int(height), int(width))

        elif name == 'square':
            width = input("Enter the width of the square: ")
            return ConcreteClass3(int(width))


def client():
    factory = Factory()
    input_for_object = input("Enter the name of the shape: ")

    object_factory = factory.create_object(input_for_object)

    print(f"The type of object created: {type(object_factory)}")
    print(f"The area of the {object_factory} is: {object_factory.abstract_method_1()}")
    print(f"The perimeter of the {object_factory} is: {object_factory.abstract_method_2()}")


client()