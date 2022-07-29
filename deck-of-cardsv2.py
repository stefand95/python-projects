from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	def __init__(self): 
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] 
		self.cards = [Card(suit, value) for suit in suits for value in values]
		print(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def __iter__(self):
		return iter(self.cards)

	def count(self):
		return len(self.cards)

	def _deal(self, number):
		count = self.count()
		actual = min([count, number])
		removed_cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		if count == 0:
			raise ValueError("All cards have been dealt")
		return removed_cards

	def deal_card(self):
		return self._deal(1)[0] 

	def deal_hand(self, number):
		return self._deal(number) 

	def shuffle(self):
		shuffle(self.cards)
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		return self

my_deck = Deck()
my_deck.shuffle()
