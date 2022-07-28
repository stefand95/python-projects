from random import shuffle

# Create Card class

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

# Create Deck class

class Deck:
	def __init__(self): #function without parameter
		# Create the deck of cards using suits list and values list
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] # "A" = 0 and "K" = 12
		self.cards = [Card(suit, value) for suit in suits for value in values]
		print(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		# Return how many cards are in the deck
		return len(self.cards)

	def _deal(self, number):
		# Store how many cards in the deck
		count = self.count()
		# Remove fewer cards from the deck if I request more cards than actually are in the deck
		actual = min([count, number])
		# Remove cards from the deck and update the deck length
		removed_cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		# Raise ValueError if there are no cards left in the deck
		if count == 0:
			raise ValueError("All cards have been dealt")
		return removed_cards

	def deal_card(self):
		return self._deal(1)[0] #returns a card as a string instead of a card as a list

	def deal_hand(self, number):
		return self._deal(number) #returns the list of cards that have been dealt as a list

	def shuffle(self):
		shuffle(self.cards)
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		return self
