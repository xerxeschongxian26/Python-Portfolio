"""
Name:    sort_Selection.py
Purpose: Sorts an array of integers suing the Selection Sort method
Author:  Xerxes Chong Xian
Method:  Selection Sort
Module Dependencies:
-NIL-
"""


def sort_Selection(array):
	print("\n")
	print(f"The input array is : {array}\n")
	length=len(array)

	for i in range(length):
		if array[i]>min(array[i:]):
			min_index=array[i:].index(min(array[i:]))+i
			array[i], array[min_index] = array[min_index], array[i]

	print("Sorting completed!\n")
	return array

if __name__=="__main__":
	print(sort_Selection([12,11,13,5,6,7,5,6,7,11,12,13]))







