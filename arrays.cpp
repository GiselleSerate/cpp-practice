// Using these exercises linked: 
// https://en.wikibooks.org/wiki/C%2B%2B_Programming/Exercises/Static_arrays/Pages

#include <iostream>

#define LENGTH 10

// Helpers.
void getUserArray(int intArray[], int length);

// Exercises.
void exercise1();
void exercise2();

int main() {
	// exercise1();
	exercise2();
	return 0;
}

// Takes a reference to an array and a length for the array. 
// Returns nothing. 
// Modifies the memory pointed to with user inputted values. 
// Multipurpose function for reading integers into array which I have been passed the reference of.
void getUserArray(int intArray[], int length) {
	std::cout << "Please input " << length << " numbers.\n";
	// TODO: No input validation.
	for(int i; i < length; i++) {
		std::cout << i << ": ";
		std::cin >> intArray[i];
	}
}

// Takes nothing.
// Returns nothing. 
// Takes LENGTH numbers from the user and determines how many of them are greater than or equal to 10. 
void exercise1() {
	std::cout << "Running exercise 1.\n"
	int userArray [LENGTH];

	// Populate array.
	getUserArray(userArray, LENGTH);

	int count = 0; 

	for(int i; i < LENGTH; i++) {
		if(userArray[i] >= 10) {
			count++;
		}
	}

	// I acknowledge in hindsight that "count" is a horrible cpp variable name.
	std::cout << count << " of your " << LENGTH << " numbers were greater than or equal to 10.\n";
}

void exercise2() {
	std::cout << "Running exercise 1.\n"
	int userArray [LENGTH];

	// Populate array.
	getUserArray(userArray, LENGTH);

	std::cout << "Please enter a number to look for in the array: ";
	std::cin >> 
}