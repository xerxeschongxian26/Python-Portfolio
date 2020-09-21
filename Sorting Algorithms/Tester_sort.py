import timeit

setup1='''
def sort_Bubble(array):
	length=len(array)
	sort=True

	while sort:
		#keep sorting
		sort=False
		for i in range(length-1):
			if array[i+1]<array[i]:
				temp=array[i]
				array[i]=array[i+1]
				array[i+1]=temp
				del temp
				sort=True
'''

setup2='''
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True

'''

setup3='''
def sort_Selection(nums):
	length=len(nums)

	for i in range(length):
		if nums[i]>min(nums[i:]):
			min_index=nums[i:].index(min(nums[i:]))+i
			nums[i], nums[min_index] = nums[min_index], nums[i]
'''

stmt1='sort_Bubble([12,11,13,5,6,7,5,11,13,5,6,7,11,13,5,6,7,11,13,5,6,7])'
stmt2='bubble_sort([12,11,13,5,6,7,5,11,13,5,6,7,11,13,5,6,7,11,13,5,6,7])'
stmt3='sort_Selection([12,11,13,5,6,7,5,11,13,5,6,7,11,13,5,6,7,11,13,5,6,7])'

n=1000000
time_bubble=timeit.timeit(stmt1,setup1,number=n)
print(time_bubble)
time_bubblesol=timeit.timeit(stmt2,setup2,number=n)
print(time_bubblesol)
time_selection=timeit.timeit(stmt3,setup3,number=n)
print(time_selection)

print("\n")
print(f"The input array is : {[12,11,13,5,6,7,5,11,13,5,6,7,11,13,5,6,7,11,13,5,6,7]}\n")
print(f"Time taken to sort array {n} times using sort_Bubble         : {time_bubble:5.3f} seconds")
print(f"Time taken to sort array {n} times using Bubble Solution     : {time_bubblesol:5.3f} seconds")
print(f"Time taken to sort array {n} times using sort_Selection      : {time_selection:5.3f} seconds")