"""
Name: factorial.py
Purpose: Function for returning factorial of a number using recursion
Author: Xerxes Chong Xian 
Method: Recursion
Module Dependencies:
-NIL-
"""

def factorial_recursion(n):
	"""
	Obtain and returns the factorial of the input n using the recursion method

	Catches and throws any errors

	"""
	if not n:
		return 1

	return n*factorial(n-1)


if __name__=='__main__':
	print('factorial_recursion.py has been called as the main function\nPrinting sample case for 10! using recursion\n')
	print(factorial_recursion(10))
