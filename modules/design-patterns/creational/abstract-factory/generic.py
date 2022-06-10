# https://stackabuse.com/abstract-factory-design-pattern-in-python/
# https://github.com/StackAbuse/abstract-factory-design-pattern-in-python/blob/main/abstract_factory_code.py

from abc import ABC, abstractmethod

class AbstractClass1(ABC):
    """
    Creates "Abstract Product A"
    """

    # Interface - Create Search Toolbar
    @abstractmethod
    def abstract_method_1(self):
        pass

    # Interface - Create Browser Window
    @abstractmethod
    def abstract_method_2(self):
        pass

class AbstractClass2(ABC):
    """
    Creates "Abstract Product B"
    """

    @abstractmethod
    # Interface - Create Messenger Window
    def abstract_method_1(self):
        pass



class ConcretClass1AbstactClass1(AbstractClass1):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Interface - Create Search Toolbar
    def abstract_method_1(self):
        print("Search Toolbar Created")

    # Interface - Create Browser Window]
    def abstract_method_2(self):
        print("Browser Window Created")


class ConcretClass1AbstactClass2(AbstractClass2):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Interface - Create Messenger Window
    def abstract_method_1(self):
        print("Messenger Window Created")

class ConcretClass2AbstactClass2(AbstractClass1):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Abstract Method of the Browser base class
    def abstract_method_1(self):
        print("Secure Browser - Search Toolbar Created")

    # Abstract Method of the Browser base class
    def abstract_method_2(self):
        print("Secure Browser - Browser Window Created")

    def concrete_method_3(self):
        print("Secure Browser - Incognito Mode Created")


class ConcretClass2AbstactClass2(AbstractClass2):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Abstract Method of the Messenger base class
    def abstract_method_1(self):
        print("Secure Messenger - Messenger Window Created")

    def abstract_method_2(self):
        print("Secure Messenger - Privacy Filter Created")

    def concrete_method_3(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")


class AbstractFactory(ABC):
    """
    The Abstract Factory
    """

    @abstractmethod
    def create_AbstractClass1_abstract_method(self):
        pass

    @abstractmethod
    def create_AbstractClass2_abstract_method(self):
        pass

class ConcreteFactory1AbstractFactory1(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_AbstractClass1_abstract_method(self):
        return ConcretClass1AbstactClass1()

    def create_AbstractClass2_abstract_method(self):
        return ConcretClass1AbstactClass2()

class ConcreteFactory2AbstractFactory1(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_AbstractClass1_abstract_method(self):
        return ConcretClass1AbstactClass1()

    def create_AbstractClass1_abstract_method(self):
        return ConcretClass1AbstactClass2()


def main():
    for factory in (ConcretClass1AbstactClass1(), ConcretClass1AbstactClass1()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()
        product_a.create_browser_window()
        product_a.create_search_toolbar()
        product_b.create_messenger_window()

if __name__ == "__main__":
    main()