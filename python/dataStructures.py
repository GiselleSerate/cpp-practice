# Import statements


def doubleArray(array):
	origLen = len(array)
	for element in array[0:origLen]:
		array.append(element)
	return array

# Main function
def main():
	cows = ["steve", "jake", "ian"]
	print("Here's the output of the doubleArray function.")
	print(doubleArray(cows))
	print("Here's cows after we called the function.")
	print(cows)

# Run main automagically
if __name__ == '__main__':
	main()