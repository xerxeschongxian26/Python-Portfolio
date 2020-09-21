"""
Name:    factorial_loop.py
Purpose: Function for returning factorial of a number using loops
Author:  Xerxes Chong Xian
Method:  Loop
Module Dependencies:
-NIL-
"""

def factorial_loop(n):
	sum=1
	for i in range(n,0,-1):
		sum*=i
	return sum

if __name__=='__main__':
	print('factorial_loop.py has been called as the main function\nPrinting sample case for 10! using loops\n')
	print(factorial_loop(10))

