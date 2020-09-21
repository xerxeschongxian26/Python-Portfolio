#1st method of importing scripts: Specifcy classes,variables to be imported
from war_Variables import suits, ranks, values
from war_Classes import Card, Player, Deck
# #2nd method of importing scripts: Import file, have to use appropriate extention of war_Classes. to call attributes
# from war_Variables import suits, ranks, values
# import war_Classes
#--------------------------------------------------------------------------------------------------
#Initialise 2 players and deal deck to them
player_one=Player('One')
player_two=Player('Two')

new_deck=Deck()
print('\n')
print(new_deck)
try:
	print('Beginning shuffle ...')
	new_deck.shuffle()
except:
	print('Shuffling Unsucessfull!')
else:
	print('Deck is now shuffled!')

for x in range(26):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())
print('\n')
print(player_one), print(player_two)
#--------------------------------------------------------------------------------------------------
counter_Round=0
game_on=True
while game_on:
	counter_Round+=1
	print(f'Round {counter_Round}, Fight!')
	#Perform hand checks, Player loses if zero
	if len(player_one.cards)==0:
		print("Player One has no more cards, Player Two wins!")
		game_on=False
		break
	if len(player_two.cards)==0:
		print("Player Two has no more cards, Player One wins!")
		game_on=False
		break
	#Hand checks passed, initialise a list for  players field hand
	player_one_FieldCard=[]
	player_two_FieldCard=[]
	player_one_FieldCard.append(player_one.remove_one())
	player_two_FieldCard.append(player_two.remove_one())

	at_war=True

	while at_war:
		if player_one_FieldCard[-1].value>player_two_FieldCard[-1].value:
			#Player One Wins,add both card to his hand
			player_one.add_cards(player_one_FieldCard)
			player_one.add_cards(player_two_FieldCard)
			at_war=False

		elif player_one_FieldCard[-1].value<player_two_FieldCard[-1].value:
			#Player Two Wins,add both cards to his hand
			player_two.add_cards(player_one_FieldCard)
			player_two.add_cards(player_two_FieldCard)
			at_war=False

		else:  #Equality means war
			print("Time for war!!!")
			if len(player_one.cards)<5:
				print('Player One has insufficient cards for war')
				print('Player Two Wins!')
				game_on=False
				break
			elif len(player_two.cards)<5:
				print('Player Two has insufficient cards for war')
				print('Player One Wins!')
				game_on=False
				break
			else:
				for n in range(5):
					player_one_FieldCard.append(player_one.remove_one())
					player_two_FieldCard.append(player_two.remove_one())