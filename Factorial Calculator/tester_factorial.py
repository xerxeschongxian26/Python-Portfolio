# from factorial import *
# from factorial_loop import *
import timeit

setup1='''
def factorial_loop(n):
	sum=1
	for i in range(n,0,-1):
		sum*=i
	return sum
'''

setup2='''
def factorial(n):
	"""
	Obtain and returns the factorial of the input n using the recursion method

	Catches and throws any errors

	"""
	if not n:
		return 1

	return n*factorial(n-1)
'''

stmt1='factorial_loop(500)'
stmt2='factorial(500)'
n=100000

time_loop=timeit.timeit(stmt1,setup1,number=n)
time_recur=timeit.timeit(stmt2,setup2,number=n)


print(f"Time taken to compute 500 factorial {n} times using loops     : {time_loop:5.3f} seconds")
print(f"Time taken to compute 500 factorial {n} times using recursion : {time_recur:5.3f} seconds")

#Report log
# learnt about the issue of limitations on recursion due to memory usage by constantly calling
# a function as compared to loops
# for large values of recursion, loops are superior