#Name: 	  sort_Bubble.py
#Purpose: Sorts an array of integers suing the Bubble sort method
#Author:  Xerxes Chong Xian
#Method:  Bubble sort
#Module Dependencies: 
#-NIL-
#Bubble Sort
# This simple sorting algorithm iterates over a list, comparing elements in pairs and swapping them until the larger elements "bubble up" to the end of the list, 
#and the smaller elements stay at the "bottom".
# Example: 
# Given array is
# 12 11 13 5 6 7
# Sorted array is
# 5 6 7 11 12 13

def shell(array):
	print("\n")
	print(f"The input array is : {array}\n")
	length=len(array)
	sort=True
	while sort:
		#keep sorting
		count=0
		for i in range(length-1):
			if array[i+1]<array[i]:
				temp=array[i]
				array[i]=array[i+1]
				array[i+1]=temp
				del temp
				count+=1
		if count==0:
			sort=False
			print("Sorting completed!\n")
	print(array)


if __name__=="__main__":
	shell([12,11,13,5,6,7,5,6,7,11,12,13])