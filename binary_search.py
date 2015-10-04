'''
Problem 1:
Write a program using iteration to determine if a value is in a sorted list (ascending order).

Problem 2:
Rewrite program using recursion.
'''

def iterative_binary_search(a_list, value):
	low = 0
	mid = len(a_list) / 2 
	high = len(a_list) 
	while low < high:
		mid = (low + high) // 2  # floor division
		if a_list[mid] == value: 
			return True
		elif a_list[mid] > value: 
			high = mid 
		elif a_list[mid] < value: 
			low = mid + 1
	return False

print iterative_binary_search([0,1,2,3,4,5], 2) == True
print iterative_binary_search([0,1,2,3,4,5], 6) == False


def recursive_binary_search(a_list, value):
	if len(a_list) == 0:
		return False

	midpoint = len(a_list) // 2 # floor division
	if a_list[midpoint] == value:
		return True
	else:
		if value < a_list[midpoint]:
			return recursive_binary_search(a_list[:midpoint], value)
		else:
			return recursive_binary_search(a_list[midpoint+1:], value)

print recursive_binary_search([0,1,2,3,4,5], 2) == True
print recursive_binary_search([0,1,2,3,4,5], 6) == False