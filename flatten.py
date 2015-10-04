'''
Problem 1:
Write a program using iteration to flatten a seqtype (list, tuple) 
into a one level seqtype. 

Problem 2:
Rewrite program using recursion.
'''
def iterative_flatten(items, seqtypes=(list, tuple)):
    for index, val in enumerate(items):
        while isinstance(items[index], seqtypes):
            items[index:index+1] = items[index]
    return items

print iterative_flatten([1,2,[3,4, [5]]]) == [1,2,3,4,5]

def recursive_flatten(items, seqtypes=(list,tuple)):
	flattened = []
	for val in items:
		if type(val) in seqtypes:
			flattened += recursive_flatten(val)
		else:
			flattened.append(val)
	return flattened

print recursive_flatten([1,2,[3,4, [5]]]) == [1,2,3,4,5]