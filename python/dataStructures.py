# Import statements
from collections import deque; 	# For...deques.

def testArrayMutability():
	'''Test array mutability.'''
	cows = ["steve", "jake", "ian"]
	print("Here's the output of the doubleArray function.")
	print(doubleArray(cows))
	print("Here's cows after we called the function.")
	print(cows)

def doubleArray(array):
	'''Append the array to itself and return it.'''
	origLen = len(array)
	for element in array[0:origLen]:
		array.append(element)
	return array

def testDeques():
	'''Take deques for a test drive.'''
	coolNums = deque([45,46,96,10])
	print("Originally, the deque contains: " + str(coolNums))
	coolNums.append(60)
	print("After appending, the deque contains: " + str(coolNums))
	coolNums.appendleft(7)
	print("After appending left (to front), the deque contains: " + str(coolNums))
	print("And at this point, its length is: " + str(len(coolNums)))
	# Iterate a deque.
	evens = deque() # Here's an empty deque. How interesting.
	for num in coolNums:
		if num % 2 == 1:
			num = 0 # I'm curious. Is this a reference? 
					# [FYI, it's not; num is a copy]
		else:
			evens.append(num)
	print("After attempting to assign 0 to the odd numbers, we get: " + 
		str(coolNums) + " but our evens array contains: " + str(evens))

# Main function
def main():
	testDeques()	

# Run main automagically
if __name__ == '__main__':
	main()