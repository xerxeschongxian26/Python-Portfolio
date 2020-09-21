"""
Name: FindPI2Digit.py
Purpose: Get the value of Pi to n number of decimal places
Author: Xerxes Chong Xian 
Method: Control of displayed decimal places using decimal module
Module Dependencies:
Math provides fast square rooting
Decimal gives the Decimal data type (default 28 places precision) which is much better than Float
"""
#Import relevant modules
from math import pi,sqrt,pow
from decimal import *
from factorial import *


def getIteratedValue(k):
	"""
	Returns the bottom term involving iteration in the Chudnovsky Algorithm.
	k-iterations gives k-1 decimal places.. Since we need k decimal places
	make iterations equal to k+1

	Parameters:
	k -- Number of Decimal Digits to get 
	"""
	k=k+1
	getcontext().prec=k 
	sum=0
	for k in range(k):
		first = Decimal(factorial(6*k))*Decimal((13591409+545140134*k))
		down  = Decimal(factorial(3*k))*Decimal((factorial(k)**3))*(Decimal(-262537412640768000)**Decimal(k))
		sum  += Decimal(first/down)
	return sum

def getValueofPi(k):
	"""

	"""
	top=Decimal(426880*Decimal(10005).sqrt())
	bottom=getIteratedValue(k)
	Pi=top/bottom

	return Pi

def shell():
	"""
	Console Function to create the interactive Shell.
	Runs only when __name__ == __main__ that is when the script is being called directly
	No return value and Parameters
	"""
	print ("Welcome to Pi Calculator. In the shell below Enter the number of digits up to which the value of Pi should be calculated or enter quit to exit")
	while True:
		print (">>> ", end='')
		entry = input()
		if entry == "quit":
			break
		if not entry.isdigit():
			print ("You did not enter a number. Try again")
		else:
			print (getValueofPi(int(entry)))


if __name__=='__main__':
	shell()


## Results Log
##05/08/2020 
## 1 is mine and 2 is solutions
# Both have precision set to 35dp
# 1 is accurate up to 28dp
# 2 is accurate up to 12dp
#1) 3.1415926535897932384626433832--8100322
#2) 3.141592653589--67496183444725239363674
#consider timing programs and finding the digit of errors for both