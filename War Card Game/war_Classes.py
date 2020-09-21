#Define all classes here
#Need classes for Card,Deck, Player
#Convention for naming: Caps for Classes and Non-Caps for variables
import random
from war_Variables import suits, ranks, values
class Card():
	#Each card should also have a value attached to allow for comparison
	def __init__(self,suit='Test',rank='Test'):
		self.suit=suit
		self.rank=rank
		self.value=values[rank]
	def __str__(self):
		return f'{self.rank} of {self.suit}'
		# return something related to printing a card value
class Player(): #creates a deck and shufffles it
	def __init__(self,name='Test'):
		self.name=name
		self.cards=[]

	def __str__(self):
		return f'PLayer {self.name} has {len(self.cards)} in hand'

	def add_cards(self,new_cards): #Account for possibility of adding 1 card or multiple card
		if type(new_cards)==type([]):   #new_cards is a list
			self.cards.extend(new_cards)
		else:  #new card is a single card object
			self.cards.append(new_cards)
	def remove_one(self):
		return self.cards.pop(0)

class Deck():   #contains information about player: name and cards in hand
	def __init__(self):
		self.all_cards=[]
	# Generate all 52 cards with nested loops. Contains Card class objects!
		for suit in suits:
			for rank in ranks:
				created_Card=Card(suit,rank)
				self.all_cards.append(created_Card)

	def __str__(self):
		return 'A deck of '+str(len(self.all_cards))+' cards from:\n'+str(self.all_cards[0]) + ' to ' + str(self.all_cards[51]) 

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop() #deals one card from end of deck
#if statement for running file individually
if __name__=='__main__':
	print('war_Classes.py is being run directly\n\nFile contains class definitions, no output expected\n')
	print(Card())
	print(Player())
	print(Deck())
else:
	print('war_Classes.py has been imported')