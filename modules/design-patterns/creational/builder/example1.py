# https://morioh.com/p/c2e1d0cdb4f8
from abc import ABC, abstractmethod

class Card:
	_cards = []

	def add(self, part: str):
		self._cards.append(part)

	def show(self):
		print('Card Built')
		for card in self._cards:
			print(card)
		print()

class abstractCard(ABC):

	@abstractmethod
	def addChip(self):
		pass

	@abstractmethod
	def addMagneticStrip(self):
		pass

	@abstractmethod
	def getCard(self):
		pass

class AbcPaymentCard(abstractCard):
	__card = Card()

	def addChip(self):
		self.__card.add('AbcPaymentCard integrated with Chip Facility')

	def addMagneticStrip(self):
		self.__card.add('AbcPaymentCard integrated with Magnetic-Strip Facility')

	def getCard(self) -> Card:
		return self.__card

class XyzPaymentCard(abstractCard):
	__card = Card()

	def addChip(self):
		self.__card.add('XyzPaymentCard integrated with Chip Facility')

	def addMagneticStrip(self):
		self.__card.add('XyzPaymentCard integrated with Magnetic-Strip Facility')

	def getCard(self) -> Card:
		return self.__card

class BankA:
	def prepareCard(self, card: abstractCard):
		card.addMagneticStrip()
		card.addChip()

class Customer:
	def MainFunc(self):
		bank = BankA()
		cardTypeAbc: abstractCard = AbcPaymentCard()
		bank.prepareCard(cardTypeAbc)
		cardAbc = cardTypeAbc.getCard()

		cardTypeXyz: abstractCard = XyzPaymentCard()
		bank.prepareCard(cardTypeXyz)
		cardXyz = cardTypeXyz.getCard()
		cardXyz.show()


if __name__ == "__main__":
	cs = Customer()
	cs.MainFunc()