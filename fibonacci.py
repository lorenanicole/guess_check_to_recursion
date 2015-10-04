'''
Problem 1:
Write a program using iteration to find the value of the nth fibonacci. 

Problem 2:
Rewrite program using recursion.
'''

def iterative_fibonacci(num):
	fib_seq = [0, 1]
	while len(fib_seq) != num+1:
		fib_seq.append(fib_seq[-2] + fib_seq[-1])
	return fib_seq[-1]

print iterative_fibonacci(11) == 89
print iterative_fibonacci(35) == 9227465


def recursive_fibonacci_one(num, seq=[0,1]):
	if len(seq) == num+1:
		return seq[-1]
	seq.append(seq[-2] + seq[-1])
	return recursive_fibonacci_one(num, seq)



print recursive_fibonacci_one(5) == 5
print recursive_fibonacci_one(11) == 89
print recursive_fibonacci_one(35) == 9227465


def recursive_fibonacci_two(num):
	if num == 1 or num == 2:
		return 1
	return recursive_fibonacci_two(num-1) + recursive_fibonacci_two(num-2)

print recursive_fibonacci_two(5) == 5
print recursive_fibonacci_two(11) == 89
print recursive_fibonacci_two(35) == 9227465