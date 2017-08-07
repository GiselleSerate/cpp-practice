// Not a very descriptive program name, but I started this file with
// no idea what I was programming. So. 

#include <iostream>
using namespace std;

void addNumbers(int *, int *);
void printNumbers(int, int);

int main() { 
	int firstNum; // These are pointers.
	int secondNum;
	addNumbers(&firstNum, &secondNum);
	printNumbers(firstNum, secondNum);
	return 0;
}

// Takes two pointers to numbers, stores the user variables in these memory locations. Returns nothing. 
// Takes in two numbers from user input and prints their sum.
// Experimenting with: I/O
void addNumbers(int *firstPtr, int *secondPtr) { 
	cout << "Please give me a number.\n";
	cin >> *firstPtr;
	cout << "I'd like another number, please.\n";
	cin >> *secondPtr;
	cout << "You have just entered numbers which sum to " << *firstPtr + *secondPtr << ".\n";
}

// Takes two numbers and prints them out.
void printNumbers(int firstNum, int secondNum) {
	cout << "We can now print the numbers you gave to a different function.\n";
	cout << firstNum << " " << secondNum << "\n";
}