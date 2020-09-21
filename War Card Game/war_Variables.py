#Define all lists and dictionaries here
suits=['Diamonds','Clubs','Hearts','Spades']
ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}    #value dictionary maps the rank of the card to a numerical values

if __name__=='__main__':
	print('war_Variables.py is being run directly\n\nFile contains some list and dictionary\n')
	print(suits)
	print(ranks)
	# print(values.items())
	for tup in values.items():  #Dictionary cannot be iterated through, use items() method to create tuple list
		# print('%5s is mapped to the value: %10sSPACE' %(tup[0],tup[1]))	
		print('{:<5} is mapped to the value: {:<6}'.format(tup[0],tup[1]))
else:
	print('war_Variables.py has been imported')